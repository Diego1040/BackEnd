from mimetypes import init
from django.db import models

# Create your models here.

class Gato:
    def __init__(self, nombre, raza, edad, genero, color, peso) -> None:
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.genero = genero
        self.color = color
        self.peso = peso

