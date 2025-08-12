from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from common.models import Subscribe
from events.models import Event


# Create your views here.
def about(request):
    return render(request, 'common/about.html')


def view_all(request):
    return render(request, 'common/view-all.html')

@login_required
def subscribe(request, event_pk):
    event = Event.objects.get(pk=event_pk)
    subscription = Subscribe.objects.filter(for_event__pk=event.pk, from_profile=request.user).first()

    if subscription:
        subscription.delete()
    else:
        Subscribe.objects.create(
            for_event=event,
            from_profile=request.user,
        )
    return redirect('event-details', pk=event.pk)


class DashboardView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'common/dashboard.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        today = timezone.now().date()
        queryset = queryset.filter(event_date__gte=today).order_by('event_date')
        return queryset
