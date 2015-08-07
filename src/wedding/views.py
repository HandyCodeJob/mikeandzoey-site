from django.shortcuts import render
from django.views import generic

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

def rsvp(request):
    context = {}
    if request.METHOD == 'POST':
        form = PersonForm(request.data)
    else:
        context.update('form', PersonForm())
    return render(request, 'core/rsvp.html', context)
