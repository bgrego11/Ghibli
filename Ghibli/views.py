# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Movie

def index(request):
    movie_list = Movie.objects.order_by('id')
    context = {
        'movie_list': movie_list,
    }

    return render(request,'Ghibli/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'Ghibli/detail.html', {'movie': movie})