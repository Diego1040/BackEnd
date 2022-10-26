# Generated by Django 4.1 on 2022-10-26 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_imdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='movie.director'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.IntegerField(default=1),
        ),
    ]
