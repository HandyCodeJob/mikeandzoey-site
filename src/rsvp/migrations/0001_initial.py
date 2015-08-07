# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('attending', models.BooleanField(default=False, verbose_name='Attending')),
                ('food_choice', models.CharField(max_length=31, verbose_name='Choice of Food', choices=[(b'hamburger', 'Hamburger'), (b'chicken', 'Chicken'), (b'veggie', 'Veggie Burger')])),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_name', models.CharField(max_length=127, verbose_name='Family Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
            ],
            options={
                'verbose_name': 'RSVP',
                'verbose_name_plural': "RSVP's",
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=127, verbose_name='Artist')),
                ('title', models.CharField(max_length=127, verbose_name='Song Title')),
                ('album', models.CharField(max_length=127, verbose_name='Album Name')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(to='rsvp.RSVP'),
        ),
    ]
