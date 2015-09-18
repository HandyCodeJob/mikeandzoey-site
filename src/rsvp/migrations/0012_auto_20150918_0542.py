# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0011_weddingevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingevent',
            name='event_tz',
            field=timezone_field.fields.TimeZoneField(verbose_name='Timezone of event', default='US/Central'),
        ),
        migrations.AlterField(
            model_name='weddingevent',
            name='location_website',
            field=models.URLField(max_length=128, verbose_name="Event location's website", null=True, blank=True),
        ),
    ]
