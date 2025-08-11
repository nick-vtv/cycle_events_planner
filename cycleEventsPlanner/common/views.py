from django.shortcuts import render
from django.views.generic import ListView

from events.models import Event


# Create your views here.
def about(request):
    return render(request, 'common/about.html')


class DashboardView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'common/dashboard.html'


