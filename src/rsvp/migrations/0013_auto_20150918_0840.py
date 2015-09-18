# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0012_auto_20150918_0542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weddingevent',
            old_name='event_discription',
            new_name='event_description',
        ),
    ]
