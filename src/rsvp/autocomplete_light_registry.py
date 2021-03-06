from django.utils.translation import ugettext as _
import autocomplete_light as al
from .models import Person


class PersonAutocomplete(al.AutocompleteModelBase):
    search_fields = ('name',)
    attrs = {
        "placeholder": _("Your name please"),
        "data-autocomplete-minimum-characters": 3,
    }
    widget_attrs = {
        "data-widget-maximum-values": 4,
    }


al.register(Person, PersonAutocomplete)
