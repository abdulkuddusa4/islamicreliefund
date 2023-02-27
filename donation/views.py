from django.shortcuts import render
from event_plans.models import EventPlan


def home(request):
    events = EventPlan.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'index.html', context)

