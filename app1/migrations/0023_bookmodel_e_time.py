# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_bookmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='e_time',
            field=models.TimeField(blank=True, default=None),
        ),
    ]
