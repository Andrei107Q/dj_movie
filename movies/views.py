from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import *


class MoviesView(ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'


# class MoviesView(View):
#     # Список фильмов
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'movies/movies.html', {'movie_list': movies})


class MovieDetailView(DetailView):
    # Описание фильма
    model = Movie
    slug_field = 'url'
    template_name = 'movies/moviesingle.html'


# class MovieDetailView(View):
#     # Описание фильма
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/moviesingle.html', {'movie': movie})
    