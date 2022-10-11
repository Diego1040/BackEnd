from multiprocessing import context
from django.shortcuts import render
from .models import Movie, Director

# Create your views here.

def home(request):

    movie_list = Movie.objects.all()

    context = {
        "movies" : movie_list
    }



    return render(request, 'movie/templates/index.html', context)
