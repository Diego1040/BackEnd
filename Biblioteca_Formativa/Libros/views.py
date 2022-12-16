from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import BookForm
from django.urls import reverse_lazy

# Create your views here.

#class BookForm(ModelForm):

    #class Meta:

        #model = Book
        #fields = ['isbn', 'title', 'year', 'description', 'category', 'author']


def home(request):

    return render(request, 'Libros/templates/home.html')

class bookListView(ListView):
    template_name = 'Libros/templates/book_list.html'
    model = Book

class BookCreate(CreateView):
    template_name = 'Libros/templates/book_form.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')


#def book_list(request):

    #listado = Book.objects.all()

    #context = {"context": listado}


    #return render(request, "Libros/templates/book_list.html", context)