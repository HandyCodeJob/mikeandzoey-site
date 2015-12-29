# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0017_auto_20151212_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeevent',
            name='date',
            field=models.CharField(max_length=128, verbose_name='Event Date'),
        ),
        migrations.AlterField(
            model_name='lifeevent',
            name='picture',
            field=models.ImageField(upload_to='', null=True, verbose_name='Event Picture'),
        ),
    ]
