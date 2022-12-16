from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from .models import *
from django.views.generic.list import ListView

# Create your views here.

#class BookForm(ModelForm):

    #class Meta:

        #model = Book
        #fields = ['isbn', 'title', 'year', 'description', 'category', 'author']


class bookListView(ListView):
    model = Book

def home(request):

    return render(request, 'Libros/templates/home.html')


#def book_list(request):

    #listado = Book.objects.all()

    #context = {"context": listado}


    #return render(request, "Libros/templates/book_list.html", context)