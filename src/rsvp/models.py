from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

FOOD_CHOICES = (
        ('hamburger', _('Hamburger')),
        ('chicken', _('Chicken')),
        ('veggie', _('Veggie Burger')),
    )

class RSVP(models.Model):
    family_name = models.CharField(_('Family Name'), max_length=127)
    email = models.EmailField(_('Email'), blank=True)

    class Meta:
        verbose_name = _('RSVP')
        verbose_name_plural = _('RSVP\'s')

    def __str__(self):
        return self.family_name

    def get_absolute_url(self):
        return "/rsvp/%i/" % self.id


class Person(models.Model):
    name = models.CharField(_('Name'), max_length=128)
    attending = models.BooleanField(_('Attending'), default=False)
    food_choice = models.CharField(_('Choice of Food'), max_length=31,
                                   blank=True, choices=FOOD_CHOICES)
    group = models.ForeignKey(RSVP)
    last_modified = models.DateField(_("Last Modified"), auto_now=True)

    class Meta:
        verbose_name_plural = _('People')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/person/%i/" % self.id


class Song(models.Model):
    artist = models.CharField(_('Artist'), max_length=127)
    title = models.CharField(_('Song Title'), max_length=127)
    album = models.CharField(_('Album Name'), max_length=127)

    def __str__(self):
        return self.title
