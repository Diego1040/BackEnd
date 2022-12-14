from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, verbose_name="ID_Categoria") #default=uuid.uuid4)
    name = models.CharField(max_length=50, verbose_name='Nombre_categoria')

    def __str__(self) -> str:
        return f"{self.name}"

class Country(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, verbose_name="ID_Cuidad") #default=uuid.uuid4)
    name = models.CharField(max_length=50, verbose_name="Nombre_Pais")

    def __str__(self) -> str:
        return f"{self.name}"

class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=200, verbose_name="Nombre autor")
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE, null=True, blank=False
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Book(models.Model):
    isbn = models.CharField(primary_key=True, verbose_name="ISBN", max_length=10)
    title = models.CharField(max_length=50, verbose_name="Nombre_Libro")
    year = models.DateField(verbose_name="Año publicacion")
    description = models.TextField()
    category = models.ManyToManyField(Category, verbose_name="Categorias")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.title}"