from django.shortcuts import render
from .forms import *
from django.views.generic.edit import CreateView

# Create your views here.

class BookCreate(CreateView):
    template_name = 'app/templates/book_edit.html'
    model = Book
    form_class = BookForm


def editar(request):




    return render(request, 'app/templates/book_edit.html')
