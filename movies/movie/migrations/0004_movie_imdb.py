# Generated by Django 4.1 on 2022-10-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_genero_paises_remove_movie_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
