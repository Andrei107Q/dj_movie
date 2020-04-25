from django.urls import path

from .views import MoviesView, MovieDetailView, AddReview


urlpatterns = [
    path('', MoviesView.as_view()),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_url'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),

]