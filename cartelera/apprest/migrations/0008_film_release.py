# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 12:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0007_remove_film_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='release',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 12, 39, 51, 555799, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
