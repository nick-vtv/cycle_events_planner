from django.shortcuts import render
from django.views.generic import ListView

from gallery.models import Photo


# Create your views here.
class GalleryListView(ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'gallery/gallery-board.html'
