
from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=10, verbose_name="Isbn")
    title = models.CharField(max_length=10, verbose_name="Titulo")
    year = models.DateField(verbose_name="Año publicacion")
    descriptions = models.TextField(verbose_name="Descripcion")

    def __str__(self):
        return self.title
