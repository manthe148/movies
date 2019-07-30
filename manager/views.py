from django.shortcuts import render
from manager.models import Movie, Genre, Director, DeliveryType, Rating
from django.views import generic
from django.views.generic import ListView

from django.db.models import Q

# Create your views here.
def index(request):

    num_visits = request.session.get('num_visits' , 0)
    request.session['num_visits'] = num_visits + 1

    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.all().count()
    num_genre = Genre.objects.all().count()

    context = {
        'num_visits': num_visits,
        'num_movies': num_movies,
        'num_directors': num_directors,
        'num_genre': num_genre,
        
    }

    return render(request, 'index.html', context= context)


class MovieListView(generic.ListView):
    model = Movie

class MovieDetailView(generic.DetailView):
    model = Movie

class SearchResultsView(generic.ListView):
    model = Movie
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(genre__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
