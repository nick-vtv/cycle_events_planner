from django.urls import path, include

from bikes.views import BikeAddView, BikeDetailView, BikeUpdateView, BikeDeleteView, BikeListView, MyBikesListView

urlpatterns = [
    path('add/', BikeAddView.as_view(), name='add-bike'),
    path('all/', BikeListView.as_view(), name='all-bikes'),
    path('my-bikes/', MyBikesListView.as_view(), name='my-bikes'),
    path('<int:pk>/', include([
        path('', BikeDetailView.as_view(), name='bike-details'),
        path('edit/', BikeUpdateView.as_view(), name='edit-bike'),
        path('delete/', BikeDeleteView.as_view(), name='delete-bike'),
    ]))
]
