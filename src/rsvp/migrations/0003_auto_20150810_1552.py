# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20150810_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='food_choice',
            field=models.CharField(verbose_name='Choice of Food', max_length=31, choices=[('hamburger', 'Hamburger'), ('chicken', 'Chicken'), ('veggie', 'Veggie Burger')], blank=True),
        ),
    ]
