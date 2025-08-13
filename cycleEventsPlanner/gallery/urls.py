from django.urls import path, include

from gallery.views import GalleryListView

urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery-board'),
    path('photos/<int:pk>/', include([

    ])),
]
