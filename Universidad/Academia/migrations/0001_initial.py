# Generated by Django 4.1.3 on 2022-11-28 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('id_carrera', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('codigo', models.IntegerField()),
                ('seccion', models.CharField(max_length=40)),
                ('docente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rut', models.TextField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('vigencia', models.BooleanField()),
                ('codigo_carrera', models.ForeignKey(null=b'I00\n', on_delete=django.db.models.deletion.CASCADE, to='Academia.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_matricula', models.IntegerField()),
                ('codigo_curso', models.IntegerField()),
                ('fecha_matricula', models.DateField()),
                ('id_estudiante', models.ForeignKey(null=b'I00\n', on_delete=django.db.models.deletion.CASCADE, to='Academia.estudiante')),
            ],
        ),
    ]
