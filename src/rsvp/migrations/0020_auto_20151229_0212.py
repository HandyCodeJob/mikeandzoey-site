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
            field=models.DateField(verbose_name='Event real date'),
        ),
    ]
