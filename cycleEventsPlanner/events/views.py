from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

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


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event-details.html'


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventEditForm
    context_object_name = 'event'
    template_name = 'events/edit-event.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().created_by.pk

    def get_success_url(self):
        return reverse('event-details', kwargs={'pk': self.object.pk})
