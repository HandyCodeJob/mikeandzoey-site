# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0019_auto_20151229_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeevent',
            name='date',
            field=models.TextField(max_length=128, verbose_name='Event real date'),
        ),
        migrations.AlterField(
            model_name='lifeevent',
            name='picture',
            field=models.ImageField(upload_to='', verbose_name='Event Picture', null=True, blank=True),
        ),
    ]
