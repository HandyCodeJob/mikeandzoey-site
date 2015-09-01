# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_auto_20150810_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('name',), 'verbose_name_plural': 'People'},
        ),
    ]
