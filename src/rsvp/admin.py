from django.contrib import admin
from reversion import VersionAdmin
from .models import RSVP, Person, Song

# Register your models here.

class PersonInline(admin.StackedInline):
    model = Person
    extra = 1

class RSVPAdmin(VersionAdmin):
    inlines = (PersonInline,)

admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Person)
admin.site.register(Song)
