from multiprocessing import context
import re
from urllib import request
from django.shortcuts import render
from .models import Movie, Director
from .forms import MovieForm, DirectorForm

# Create your views here.

def home(request):

    movie_list = Movie.objects.all()
    director_list = Director.objects.all()

    context = {
        "movies" : movie_list ,
        "directors" : director_list
    }

    return render(request, 'movie/templates/index.html', context)


def add_movie(request):
    form = MovieForm()
    context = {
        'titulo': 'Pelicula',
        'form': form
        
    }
    
    return render(request, 'movie/templates/index2.html', context)



def add_director(request):
    form = DirectorForm()
    context = {
        'titulo': 'Director',
        'form': form
        
    }
    
    return render(request, 'movie/templates/index2.html', context)
