# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ghibli', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
    ]
