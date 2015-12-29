# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0018_auto_20151229_0142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lifeevent',
            options={'ordering': ('-date',), 'verbose_name_plural': 'Life Events'},
        ),
        migrations.AddField(
            model_name='lifeevent',
            name='date_text',
            field=models.CharField(verbose_name='Event Date', default='', max_length=128),
            preserve_default=False,
        ),
    ]
