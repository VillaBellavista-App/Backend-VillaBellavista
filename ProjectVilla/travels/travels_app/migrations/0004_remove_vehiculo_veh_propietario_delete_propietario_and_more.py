# Generated by Django 4.2.3 on 2023-07-13 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels_app', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='veh_propietario',
        ),
        migrations.DeleteModel(
            name='Propietario',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]