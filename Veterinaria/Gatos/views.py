from cgitb import html
from http.client import HTTPResponse
from urllib import request, response
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def gatos(request):
    
    
    return render(request, './Gatos/Templates/Bienvenida.html')

def form(request):

    return render(request, './Gatos/Templates/Formulario.html')

def lista(request):

    dic = {
        'gatos' : [
            {'nombre' : 'simon', 'raza': '?', 'edad' : '4y', 'Genero' : 'Macho', 'Color': 'Marron', 'Peso': '8Kg'},
            {'nombre' : 'simon', 'raza': '?', 'edad' : '3y', 'Genero' : 'Macho', 'Color': 'Marron', 'Peso': '8Kg'},
            {'nombre' : 'simon', 'raza': '?', 'edad' : '2y', 'Genero' : 'Macho', 'Color': 'Marron', 'Peso': '8Kg'},
            {'nombre' : 'simon', 'raza': '?', 'edad' : '4y', 'Genero' : 'Macho', 'Color': 'Marron', 'Peso': '8Kg'}
        ]
    }

    return render(request, './Gatos/Templates/Listado.html', dic)

