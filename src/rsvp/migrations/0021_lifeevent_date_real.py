# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0020_auto_20151229_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifeevent',
            name='date_real',
            field=models.DateField(default=datetime.datetime(2015, 12, 29, 2, 32, 10, 834104, tzinfo=utc), verbose_name='Event date for sorting'),
            preserve_default=False,
        ),
    ]
