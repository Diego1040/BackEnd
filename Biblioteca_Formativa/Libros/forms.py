from django import forms
from django.forms import ModelForm
from .models import *


class BookForm(ModelForm):

    class Meta:

        model = Book
        fields = ['isbn', 'title', 'year', 'description', 'category', 'author']
        widgets = {
            'isbn': forms.TextInput(attrs={"class":"form-control", "pleaceholder": "Isbn"}),
            'title': forms.TextInput(attrs={"class":"form-control", "pleaceholder": "Title"}),
            'year': forms.DateInput(attrs={"class":"form-control", "type": "date"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),
            'category': forms.SelectMultiple(attrs={"class":"select form-control"}),
            'author': forms.Select(attrs={"class":"form-control"})
        }
