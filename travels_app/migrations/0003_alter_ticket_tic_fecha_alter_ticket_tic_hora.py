# Generated by Django 4.2.1 on 2023-09-10 01:58

import datetime
from django.db import migrations, models
import travels_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('travels_app', '0002_alter_ticket_tic_fecha_alter_ticket_tic_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tic_fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tic_hora',
            field=models.TimeField(default=travels_app.models.get_current_time),
        ),
    ]
