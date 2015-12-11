from django.shortcuts import render, HttpResponse
from .forms import PersonForm, GroupForm, AdditionalPersonForm
from .models import Person
# Create your views here.


def rsvp(request):
    context = {}
    if request.method == "POST":
        """
        Have to first decode the byte stream, then split it on the csrf. The
        first one is blank, so we cut that off. Then we take each of those
        entries and split them so that we get 'key=value' in a lit. We remove
        the token as we do not need it. There can be a blank pair, so we skip
        that as well. If we cannot find the name, then we create that person,
        add them to the group that is the same as the first person. We then
        remove on of the plus one's as they have already filled in the name.
        """
        post = request.body.decode('utf-8').split('csrfmiddlewaretoken')[1:]
        people_list = []
        for person in post:
            data = person.split('&')[1:]
            person_data = {}
            for entry in data:
                if entry:
                    raw = entry.split('=')
                    pair = {raw[0]: raw[1].replace('+', ' ')}
                if pair:
                    person_data.update(pair)
            people_list.append(person_data)
        for person_data in people_list:
            print(person_data)
            try:
                person = Person.objects.get(name=person_data['name'])
            except Person.DoesNotExist:
                if person_data['name']:
                    person = Person(**person_data)
                    linked_person = Person.objects.get(name=people_list[0]['name'])
                    linked_person.group.additonal_allowed -= 1
                    person.group = linked_person.group
                    person.group.save()
                    person.save()
                else:
                    print("null person")
            else:
                person.food_choice = person_data['food_choice']
                person.save()
        return HttpResponse("Done")
    else:
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
        form = PersonForm(instance=member)
        forms.append(form)
    for i in range(group.additonal_allowed):
        form = AdditionalPersonForm(initial={'attending': True})
        forms.append(form)
    context['forms'] = forms
    context['plus_one'] = group.additonal_allowed
    return render(request, 'rsvp/choices.html', context)
