# Generated by Django 5.0.6 on 2024-07-07 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoPython', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField()),
                ('mayorista', models.CharField(max_length=50)),
            ],
        ),
    ]
