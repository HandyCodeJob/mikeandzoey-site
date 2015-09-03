from django.shortcuts import render, HttpResponse
from .forms import PersonForm, GroupForm
from .models import Person
# Create your views here.


def rsvp(request):
    context = {}
    group = GroupForm()
    context['group_form'] = group
    return render(request, 'rsvp/rsvp.html', context)

def person_autocomplete(request,
    template_name='autocomplete_light/model_template/choice.html'):
    q = request.GET.get('q', '')
    context = {'q': q}
    queries = {}
    queries['people'] = Person.objects.filter(name__icontains=q)[:3]
    context.update(queries)
    return shortcuts.render(request, template_name, context)

def person(request, name):
    person = Person.objects.get(name=name)
    group = person.group
    forms = []
    context = {}
    for member in group.family_member.all():
        form = PersonForm(initial={'name': member.name})
        forms.append(form)
    context['forms'] = forms
    return render(request, 'rsvp/choices.html', context)
