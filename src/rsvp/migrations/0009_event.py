# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0008_auto_20150906_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Event Title')),
                ('text', models.TextField(verbose_name='Event Description')),
                ('date', models.DateField(verbose_name='Event Date')),
                ('picture', models.ImageField(upload_to='', verbose_name='Event Picture')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
