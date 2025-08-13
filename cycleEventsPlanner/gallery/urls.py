from django.urls import path, include

from gallery.views import GalleryListView, GalleryPhotoAddView

urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery-board'),
    path('add/', GalleryPhotoAddView.as_view(), name='gallery-add-photo'),
    path('photos/<int:pk>/', include([

    ])),
]
