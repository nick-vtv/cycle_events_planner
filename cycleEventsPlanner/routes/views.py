from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from routes.forms import RouteCreateForm, RouteEditForm
from routes.models import Route


# Create your views here.
class RouteAddView(LoginRequiredMixin, CreateView):
    model = Route
    form_class = RouteCreateForm
    template_name = 'routes/add-route.html'
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    context_object_name = 'routes'
    template_name = 'routes/routes-list.html'


class RouteDetailView(LoginRequiredMixin, DetailView):
    model = Route
    context_object_name = 'route'
    template_name = 'routes/route-details.html'


class RouteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Route
    form_class = RouteEditForm
    context_object_name = 'route'
    template_name = 'routes/edit-route.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().created_by.pk

    def get_success_url(self):
        return reverse('route-details', kwargs={'pk': self.object.pk})
