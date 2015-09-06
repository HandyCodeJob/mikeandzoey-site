from django import forms
import autocomplete_light
from .models import RSVP, Person, Song

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineField, InlineRadios
from crispy_forms.layout import Layout, Button

class GroupForm(forms.Form):
    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineField('name'),
            Button('set', 'Set'),
        )

    class Meta:
        widgets = {
            "name": autocomplete_light.TextWidget("PersonAutocomplete"),
        }


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ('email',)


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'album')


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            InlineField('name', readonly=True),
            InlineField('food_choice'),
        )

    class Meta:
        model = Person
        fields = ('name', 'food_choice',)

class AdditionalPersonForm(PersonForm):
    def __init__(self, *args, **kwargs):
        super(AdditionalPersonForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            InlineField('name'),
            InlineField('food_choice'),
        )
