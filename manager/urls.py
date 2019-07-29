from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('movies', views.MovieListView.as_view(), name='movies'),
    path('movies/<pk>', views.MovieDetailView.as_view(), name='movie-detail'),
    path('search/', views.SearchResultsView.as_view(), name = 'search-results'),
]