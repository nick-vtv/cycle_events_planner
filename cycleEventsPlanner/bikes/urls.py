from django.urls import path

from bikes.views import BikeAddView

urlpatterns = [
    path('add/', BikeAddView.as_view(), name='add-bike'),

]
