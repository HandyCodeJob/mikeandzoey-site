from django.shortcuts import render
from django.views import generic
from rsvp.models import Event

# Create your views here.

class HomePage(generic.View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        return render(request, self.template_name, {'events': events})


class AboutPage(generic.TemplateView):
    template_name = "about.html"

