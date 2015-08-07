from django.forms import ModelForm
from .models import RSVP, Person, Song

class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = ('email',)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'attending', 'food_choice',)

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'album')
