
from django import forms
from django.forms import ModelForm
from .models import Movie, Director

class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'comment', 'imdb']


class DirectorForm(ModelForm):

    class Meta:
        model = Director
        fields = ['name', 'last_name']