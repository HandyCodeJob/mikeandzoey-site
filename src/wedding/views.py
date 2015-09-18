from django.shortcuts import render
from django.views import generic
import math
from collections import OrderedDict
from rsvp.models import LifeEvent, WeddingEvent, Logistics

# Create your views here.


class HomePage(generic.View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        events = LifeEvent.objects.all()
        return render(request, self.template_name, {'events': events})


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class WeddingPage(generic.TemplateView):
    template_name = "wedding.html"

    def get(self, request, *args, **kwargs):
        """
        Seprates the events into a dict with keys of dates and values as lists
        that contain the events that start during that date.
        """
        events = WeddingEvent.objects.all()
        days = OrderedDict()
        for event in events:
            days.setdefault(event.event_start.date(), []).append(event)
            if event.main_event:
                main_event = event
        col_size = 3 if len(days) == 4 else None  # 4 days is 3 col
        col_size = 4 if col_size else 6  # 3 days is 4 col, 2 days is 6 col
        return render(request, self.template_name, {
            'events': events,
            'days': days,
            'col_size': col_size,
            'main_event': main_event,
        })


class LogisticsPage(generic.TemplateView):
    template_name = "logistics.html"

    def get(self, request, *args, **kwargs):
        travels = Logistics.objects.filter(section='travel')
        hotels = Logistics.objects.filter(section='hotel')
        outings = Logistics.objects.filter(section='outing')
        return render(request, self.template_name, {
            'travels': travels,
            'hotels': hotels,
            'outings': outings,
        })

