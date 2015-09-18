# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0009_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='LifeEvent',
        ),
        migrations.AlterModelOptions(
            name='lifeevent',
            options={'ordering': ('date',), 'verbose_name_plural': 'Life Events'},
        ),
    ]
