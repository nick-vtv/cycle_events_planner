from django.urls import path, include

from routes.views import RouteAddView, RouteDetailView, RouteUpdateView

urlpatterns = [
    path('add/', RouteAddView.as_view(), name='add-route'),
        path('<int:pk>/', include([
            path('', RouteDetailView.as_view(), name='route-details'),
            path('edit/', RouteUpdateView.as_view(), name='edit-route'),
        ]))
]
