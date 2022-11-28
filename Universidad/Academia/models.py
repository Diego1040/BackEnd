from pickle import FALSE
from random import choices
from xml.dom.minidom import DocumentType
from django.db import models

# Create your models here.


class Carrera(models.Model):
    name = models.CharField(max_length=50)
    duracion = models.IntegerField()
    id_carrera = models.CharField(max_length=10)

    def __str__(self):
        return self.name



class Estudiante(models.Model):
    name = models.CharField(max_length=50)
    rut = models.TextField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    #sexos = [
        #('F', 'femenino')
        #('M', 'masculino')
    #]

    #sexo = models.CharField(max_length=1, choices=sexos,default='F')
    sexo = models.CharField(max_length=15)
    correo = models.EmailField()
    vigencia = models.BooleanField()
    codigo_carrera = models.ForeignKey(
        'Carrera', on_delete=models.CASCADE, null=FALSE
    )

    def __str__(self):
        return f'{self.name} -- {self.vigencia}'


class Curso(models.Model):
    name = models.CharField(max_length=50)
    codigo = models.IntegerField()
    seccion = models.CharField(max_length=40)
    docente = models.CharField(max_length=100)


class Matricula(models.Model):

    codigo_matricula = models.IntegerField()
    id_estudiante = models.ForeignKey(
        'Estudiante', 
        on_delete=models.CASCADE,null=FALSE
    )
    codigo_curso = models.IntegerField()
    fecha_matricula = models.DateField()
