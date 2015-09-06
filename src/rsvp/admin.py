#from .autocomplete_light_registry import * # NOQA
import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
from .models import RSVP, Person, Song
from .forms import PersonForm
from reversion import VersionAdmin


# Register your models here.

class PersonInline(admin.StackedInline):
    model = Person
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    model = Person
    form = PersonForm
    list_display = ('name', 'food_choice', 'group',)


class RSVPAdmin(VersionAdmin):
    inlines = (PersonInline,)


admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Song)
