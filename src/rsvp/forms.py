from django.forms import ModelForm
import autocomplete_light
from .models import RSVP, Person, Song


class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = ('email',)


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'album')


class PersonForm(ModelForm):
    class Meta:
        model = Person
        autocomplete_fields = ('name',)
        fields = ('name', 'attending', 'food_choice',)
        widgets = {
            "name": autocomplete_light.TextWidget("PersonAutocomplete"),
        }
