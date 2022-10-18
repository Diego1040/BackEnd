from multiprocessing import context
from django.shortcuts import render
from .models import Movie, Director
from .forms import MovieForm

# Create your views here.

def home(request):

    movie_list = Movie.objects.all()
    director_list = Director.objects.all()

    context = {
        "movies" : movie_list ,
        "directors" : director_list
    }

    return render(request, 'movie/templates/index.html', context)


def add(request):

    form = MovieForm()


    return render(request, 'movie/templates/index2.html',
    {'form' : form}
    )

