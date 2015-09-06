# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0007_auto_20150906_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='attending',
        ),
        migrations.AlterField(
            model_name='person',
            name='food_choice',
            field=models.CharField(choices=[('not_attending', 'Not Attending'), ('hamburger', 'Hamburger'), ('chicken', 'Chicken'), ('veggie', 'Veggie Burger')], max_length=31, verbose_name='Choice of Food', blank=True),
        ),
    ]
