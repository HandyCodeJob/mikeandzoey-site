# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0013_auto_20150918_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128, verbose_name='Heading')),
                ('section', models.CharField(choices=[('travel', 'Travel'), ('hotel', 'Hotel'), ('outing', 'Outing')], max_length=32, verbose_name='Logistics type')),
                ('description', models.TextField(blank=True, verbose_name='Body of option')),
                ('name', models.CharField(max_length=128, verbose_name='Name of the location')),
                ('website', models.URLField(null=True, blank=True, max_length=128, verbose_name="The location's website")),
            ],
            options={
                'ordering': ('section', 'name'),
                'verbose_name_plural': 'Logistics',
            },
        ),
    ]
