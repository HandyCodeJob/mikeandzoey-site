# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0015_auto_20150918_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='title',
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.CharField(verbose_name='Song Slug', max_length=255, default=' '),
            preserve_default=False,
        ),
    ]
