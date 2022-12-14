# Generated by Django 4.1.1 on 2022-12-13 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre_Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, verbose_name='ID_Categoria')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, verbose_name='ID_Cuidad')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre_Cuidad')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='ISBN')),
                ('title', models.CharField(max_length=50, verbose_name='Nombre_Libro')),
                ('year', models.DateField()),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libros.author')),
                ('category', models.ManyToManyField(to='Libros.category', verbose_name='Categorias')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libros.country'),
        ),
    ]
