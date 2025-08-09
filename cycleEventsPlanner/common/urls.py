from django.urls import path

from common.views import about

urlpatterns = [
    path('about/', about, name='about'),
]
