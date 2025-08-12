from django.urls import path

from common.views import about, DashboardView, view_all, subscribe

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('about/', about, name='about'),
    path('all/', view_all, name='view-all'),
    path('subscribe/<int:event_pk>/', subscribe, name='subscribe'),
]
