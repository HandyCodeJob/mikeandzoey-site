# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0010_auto_20150918_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeddingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='Event Title')),
                ('main_event', models.BooleanField(default=False, verbose_name='Main Event, ie Ceremony')),
                ('clean_name', models.CharField(max_length=128, verbose_name='Short name for links')),
                ('event_start', models.DateTimeField(verbose_name='Event Start Time')),
                ('event_end', models.DateTimeField(null=True, verbose_name='Event End Time')),
                ('event_tz', timezone_field.fields.TimeZoneField(verbose_name='Timezone of event')),
                ('event_note', models.TextField(blank=True, verbose_name='Event Note')),
                ('event_discription', models.TextField(verbose_name='Event Description')),
                ('location_name', models.CharField(max_length=128, verbose_name='Event Location')),
                ('location_addr', models.TextField(max_length=256, verbose_name='Event address formated')),
                ('location_map', models.URLField(max_length=512, verbose_name='Event location map url')),
                ('location_website', models.URLField(null=True, max_length=128, verbose_name="Event location's website")),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('event_start',),
                'verbose_name_plural': 'Wedding Events',
            },
        ),
    ]
