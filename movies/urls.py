from django.urls import path

from .views import MoviesView, MovieDetailView, AddReview, ActorView, FilterMoviesView, JsonFinterMoviesView, AddStarRating, Search


urlpatterns = [
    path('', MoviesView.as_view()),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('search/', Search.as_view(), name='search'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path('json-filter/', JsonFinterMoviesView.as_view(), name='json_filter'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_url'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>', ActorView.as_view(), name='actor_detail'),

]