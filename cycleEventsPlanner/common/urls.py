from django.urls import path

from common.views import about, DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('about/', about, name='about'),
]
