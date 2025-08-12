from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from bikes.forms import BikeCreateForm, BikeEditForm
from bikes.models import Bike


# Create your views here.
class BikeAddView(LoginRequiredMixin, CreateView):
    model = Bike
    form_class = BikeCreateForm
    template_name = 'bikes/add-bike.html'
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class BikeListView(LoginRequiredMixin, ListView):
    model = Bike
    context_object_name = 'bikes'
    template_name = 'bikes/bikes-list.html'


class BikeDetailView(LoginRequiredMixin, DetailView):
    model = Bike
    context_object_name = 'bike'
    template_name = 'bikes/bike-details.html'


class BikeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bike
    form_class = BikeEditForm
    context_object_name = 'bike'
    template_name = 'bikes/edit-bike.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk

    def get_success_url(self):
        return reverse('bike-details', kwargs={'pk': self.object.pk})


class BikeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bike
    context_object_name = 'bike'
    success_url = reverse_lazy('about')
    template_name = 'bikes/delete-bike.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk
