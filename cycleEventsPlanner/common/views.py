from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView

from events.models import Event


# Create your views here.
def about(request):
    return render(request, 'common/about.html')


class DashboardView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'common/dashboard.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        today = timezone.now().date()
        queryset = queryset.filter(event_date__gte=today).order_by('event_date')
        return queryset
