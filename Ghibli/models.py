# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot = models.CharField(max_length=1000)
    score = models.CharField(max_length=10)
    image_url = models.CharField(max_length=200)
    rel_year = models.CharField(max_length=5)
    def __str__(self):
        return self.title