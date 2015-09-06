# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_auto_20150902_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='attending',
            field=models.NullBooleanField(default=None, verbose_name='Attending'),
        ),
    ]
