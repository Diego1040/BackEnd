# Generated by Django 4.1.3 on 2022-12-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=10)),
                ('year', models.DateField()),
                ('descriptions', models.TextField()),
            ],
        ),
    ]
