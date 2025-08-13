from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from gallery.forms import GalleryPhotoAddForm
from gallery.models import Photo


# Create your views here.
class GalleryListView(ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'gallery/gallery-board.html'


class GalleryPhotoAddView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = GalleryPhotoAddForm
    template_name = 'gallery/add-photo.html'
    success_url = reverse_lazy('gallery-board')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)
