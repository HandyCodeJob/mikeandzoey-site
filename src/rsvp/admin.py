# from .autocomplete_light_registry import * # NOQA
import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
from .models import RSVP, Person, Song, LifeEvent, WeddingEvent, Logistics
from .forms import PersonForm, LifeEventForm, WeddingEventForm
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


class LifeEventAdmin(admin.ModelAdmin):
    model = LifeEvent
    form = LifeEventForm
    list_display = ('title', 'date',)


class WeddingEventAdmin(admin.ModelAdmin):
    model = WeddingEvent
    form = WeddingEventForm
    list_display = ('title', 'event_start',)


class LogisticsAdmin(admin.ModelAdmin):
    model = Logistics
    list_display = ('title', 'section',)

admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(LifeEvent, LifeEventAdmin)
admin.site.register(WeddingEvent, WeddingEventAdmin)
admin.site.register(Logistics, LogisticsAdmin)
admin.site.register(Song)
