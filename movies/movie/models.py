
from email.policy import default
from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    director = models.ForeignKey(
        'Director', 
        on_delete=models.CASCADE
        )
    actores = models.ManyToManyField(
        'Actor'
    )
    imdb = models.IntegerField(default=1)
    
    

    def __str__(self):
        return self.name
    
class Director(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name+ " " +self.last_name
        

class Paises(models.Model):
    name = models.CharField(max_length=100)


class Genero(models.Model):
    name = models.CharField(max_length=100)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
