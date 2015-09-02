from django.shortcuts import render
from .forms import PersonForm
# Create your views here.


def rsvp(request):
    context = {}
    if request.method == 'POST':
        form = PersonForm(request.data)
    else:
        form = PersonForm()
    context['form'] = form
    return render(request, 'rsvp/rsvp.html', context)
