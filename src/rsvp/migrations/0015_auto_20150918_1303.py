# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0014_logistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistics',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Name of the location', null=True),
        ),
    ]
