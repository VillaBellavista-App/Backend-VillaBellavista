# Generated by Django 4.2.3 on 2023-07-13 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels_app', '0005_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Destino',
            new_name='Destination',
        ),
        migrations.RenameModel(
            old_name='Propietario',
            new_name='Owner',
        ),
        migrations.RenameModel(
            old_name='Vehiculo',
            new_name='Vehicule',
        ),
    ]
