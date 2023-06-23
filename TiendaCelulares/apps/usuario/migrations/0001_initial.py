# Generated by Django 4.2.2 on 2023-06-23 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='static/celulares/')),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
