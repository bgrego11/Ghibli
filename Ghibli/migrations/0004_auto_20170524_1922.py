# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ghibli', '0003_remove_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.CharField(max_length=1000),
        ),
    ]
