# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0006_auto_20150906_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='additonal_allowed',
            field=models.IntegerField(verbose_name="Number of 'plus ones' allowed", default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='attending',
            field=models.NullBooleanField(verbose_name='Attending', default=None, choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
