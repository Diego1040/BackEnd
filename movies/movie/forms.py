
from django import forms
from django.forms import ModelForm
from .models import Movie, Director

class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'comment', 'director', 'actores', 'imdb']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control", "pleaceholder": "name"}),
            'comment': forms.Textarea(attrs={"class":"form-control", "pleaceholder": "comment"}),
            'director' : forms.Select(attrs={'class': "form-control"}),
            'actores' : forms.SelectMultiple(attrs={'class': "select form-control"}),
            'imdb': forms.NumberInput(attrs={"class":"form-control"}),
        }


class DirectorForm(ModelForm):

    class Meta:
        model = Director
        fields = ['name', 'last_name']