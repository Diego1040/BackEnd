from django.shortcuts import render

from django import forms
from django.forms import ModelForm
from .models import *

# Create your views here.

class BibliotecaForm(ModelForm):

    class Meta:

        model = Book
        fields = ['isbn', 'title', 'year', 'description', 'category', 'author']


def home(request):


    return render(request)