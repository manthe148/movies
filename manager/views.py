from django.shortcuts import render
from manager.models import Movie, Genre, Director, DeliveryType
from django.views import generic

# Create your views here.
def index(request):

    num_visits = request.session.get('num_visits' , 0)
    request.session['num_visits'] = num_visits + 1

    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.all().count()

    context = {
        'num_visits': num_visits,
        'num_movies': num_movies,
        'num_directors': num_directors,
    }

    return render(request, 'index.html', context= context)