from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Category, Actor
from .forms import ReviewForm


class MoviesView(ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'

    # def get_context_date(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


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


class AddReview(View):
    # Отзывы
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)    # узнаем к какому фильму привузять отзыв
        if form.is_valid():     # проверяем валидность формы полученной с сайта
            form = form.save(commit=False)   # приостановили сохранение формы
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie     # передает id филтма
            form.save()
        return redirect(movie.get_absolute_url())   # формируем адрес страницы на которой оставили отзыв


class ActorView(DetailView):
    # выводи информацию об актере
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'     # поле по которому проходит поиск




