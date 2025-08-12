from django.urls import path

from common.views import about, DashboardView, view_all

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('about/', about, name='about'),
    path('all/', view_all, name='view-all'),
]
