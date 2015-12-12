# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0016_auto_20151211_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.CharField(verbose_name='Request a song', max_length=255, blank=True),
        ),
    ]
