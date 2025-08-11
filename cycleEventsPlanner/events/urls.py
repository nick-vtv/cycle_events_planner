from django.urls import path, include

from events.views import EventAddView, EventDetailView, EventUpdateView

urlpatterns = [
    path('add/', EventAddView.as_view(), name='add-event'),
        path('<int:pk>/', include([
            path('', EventDetailView.as_view(), name='event-details'),
            path('edit/', EventUpdateView.as_view(), name='edit-event'),
        ]))
]
