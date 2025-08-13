from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from common.forms import CommentCreateForm
from common.models import Subscribe
from events.forms import EventCreateForm, EventEditForm
from events.models import Event


# Create your views here.
class EventAddView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'events/add-event.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/events-list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-event_date')
        return queryset


class MyEventsListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/my-events.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(created_by__pk=self.request.user.pk)
        return queryset


class MySubscribedEventsListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/subscribed-events.html'

    def get_queryset(self):
        queryset = Event.objects.filter(subscribed__from_profile__pk=self.request.user.pk).order_by('event_date')
        return queryset


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event-details.html'
    form_class = CommentCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subscription = Subscribe.objects.filter(for_event__pk=self.get_object().pk, from_profile__pk=self.request.user.pk).first()
        if subscription:
            context.update({
                'all_comments': self.object.event_comments.all(),
                'form': self.form_class,
                'is_subscribed': subscription
            })
        else:
            context.update({
                'all_comments': self.object.event_comments.all(),
                'form': self.form_class
            })
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = self.form_class(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.created_by = self.request.user
            comment.for_event = self.object
            comment.save()
            return redirect('event-details', pk=self.object.pk)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventEditForm
    context_object_name = 'event'
    template_name = 'events/edit-event.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().created_by.pk

    def get_success_url(self):
        return reverse('event-details', kwargs={'pk': self.object.pk})
