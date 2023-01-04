# Generated by Django 4.1.3 on 2022-12-17 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apodo', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('diminutivo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('colores', models.CharField(max_length=30)),
                ('diminutivo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=30)),
                ('tamanio', models.IntegerField()),
                ('peso', models.IntegerField()),
            ],
        ),
    ]
