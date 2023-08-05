# Generated by Django 4.2.1 on 2023-08-05 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travels_app', '0006_rename_destino_destination_rename_propietario_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('tar_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('tar_tarifa', models.IntegerField()),
                ('tar_nro_asientos', models.IntegerField()),
                ('tar_categoria', models.CharField(max_length=3)),
                ('tar_destino', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('user_nombre', models.CharField(max_length=20)),
                ('user_apellidos', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=30)),
                ('user_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='veh_categoria',
            field=models.CharField(max_length=3),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('tic_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('tic_hora', models.DateTimeField(auto_now_add=True)),
                ('tic_tarifa', models.ForeignKey(db_column='tic_tarifa', on_delete=django.db.models.deletion.DO_NOTHING, to='travels_app.tarifa')),
                ('tic_vehiculo', models.ForeignKey(db_column='tic_vehiculo', on_delete=django.db.models.deletion.DO_NOTHING, to='travels_app.vehicule')),
            ],
        ),
    ]