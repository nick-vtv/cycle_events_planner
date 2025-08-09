from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from bikes.forms import BikeCreateForm
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


