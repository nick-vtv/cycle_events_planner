from django.urls import path, include

from routes.views import RouteAddView, RouteDetailView, RouteUpdateView, RouteListView

urlpatterns = [
    path('add/', RouteAddView.as_view(), name='add-route'),
    path('all/', RouteListView.as_view(), name='all-routes'),
            path('<int:pk>/', include([
            path('', RouteDetailView.as_view(), name='route-details'),
            path('edit/', RouteUpdateView.as_view(), name='edit-route'),
        ]))
]
