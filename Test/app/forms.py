from django.forms import ModelForm
from django import forms
from .models import *


class BookForm(ModelForm):
    
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'year', 'description', 'category', 'author']
        widwets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'pleaceholder' : 'Isbn'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'pleaceholder': 'title'}),
            'year': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'category' : forms.SelectMultiple(attrs={'class': 'select form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'})
        }