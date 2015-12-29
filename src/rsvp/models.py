from django.db import models
from timezone_field import TimeZoneField
from django.utils.translation import ugettext as _

# Create your models here.

FOOD_CHOICES = (
    ('not_attending', _('Not Attending')),
    ('hamburger', _('Hamburger')),
    ('chicken', _('Chicken')),
    ('veggie', _('Veggie Burger')),
)

LOGISTICS_CHOICES = (
    ('travel', _('Travel')),
    ('hotel', _('Hotel')),
    ('outing', _('Outing')),
)


class RSVP(models.Model):
    family_name = models.CharField(_('Family Name'), max_length=127)
    additonal_allowed = models.IntegerField(_("Number of 'plus ones' allowed"),
                                            default=0)
    email = models.EmailField(_('Email'), blank=True)

    class Meta:
        verbose_name = _('RSVP')
        verbose_name_plural = _('RSVP\'s')

    def __str__(self):
        string = self.family_name
        if self.family_member.count() > 1:
            people = [person.name
                      for person
                      in self.family_member.exclude(name=self.family_name)]
            string += " & " + str(people)
        if self.additonal_allowed > 0:
            string += " +%i" % self.additonal_allowed
        return string


class Person(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    food_choice = models.CharField(_('Choice of Food'), max_length=31,
                                   blank=True, choices=FOOD_CHOICES)
    group = models.ForeignKey(RSVP, related_name="family_member")
    last_modified = models.DateField(_("Last Modified"), auto_now=True)

    class Meta:
        verbose_name_plural = _('People')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/person/%i/" % self.id


class Song(models.Model):
    slug = models.CharField(_('Request a song'), max_length=255, blank=True)

    def __str__(self):
        return self.slug


class LifeEvent(models.Model):
    title = models.CharField(_('Event Title'), max_length=128)
    text = models.TextField(_('Event Description'))
    date_text = models.CharField(_('Event Date'), max_length=128)
    date = models.DateField(_('Event real date'))
    picture = models.ImageField(_('Event Picture'), null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = _('Life Events')
        ordering = ('-date',)

    def get_absolute_url(self):
        return "/#%s" % self.slug


class WeddingEvent(models.Model):
    title = models.CharField(_('Event Title'), max_length=128)
    main_event = models.BooleanField(_('Main Event, ie Ceremony'),
                                     default=False)
    clean_name = models.CharField(_('Short name for links'), max_length=128)
    event_start = models.DateTimeField(_('Event Start Time'))
    event_end = models.DateTimeField(_('Event End Time'), null=True)
    event_tz = TimeZoneField(verbose_name=_('Timezone of event'),
                             default='US/Central')
    event_note = models.TextField(_('Event Note'), blank=True)
    event_description = models.TextField(_('Event Description'))
    location_name = models.CharField(_('Event Location'), max_length=128)
    location_addr = models.TextField(_('Event address formated'),
                                     max_length=256)
    location_map = models.URLField(_('Event location map url'), max_length=512)
    location_website = models.URLField(_("Event location's website"),
                                       max_length=128,
                                       blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = _('Wedding Events')
        ordering = ('event_start',)

    def get_absolute_url(self):
        return "/#%s" % self.slug


class Logistics(models.Model):
    title = models.CharField(_('Heading'), max_length=128)
    section = models.CharField(_('Logistics type'),
                               choices=LOGISTICS_CHOICES,
                               max_length=32)
    description = models.TextField(_('Body of option'), blank=True)
    name = models.CharField(_('Name of the location'),
                            blank=True, null=True,
                            max_length=128)
    website = models.URLField(_("The location's website"),
                              max_length=128,
                              blank=True, null=True)

    class Meta:
        verbose_name_plural = _('Logistics')
        ordering = ('section', 'name',)
