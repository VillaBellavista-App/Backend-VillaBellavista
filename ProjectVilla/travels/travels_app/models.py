from django.db import models
from datetime import date, datetime

# Functions for models

def get_current_time():
    return datetime.now().time()

# Models 

class Owner(models.Model):
    prop_id = models.SmallAutoField(primary_key=True)
    prop_nombre = models.CharField(max_length=50)
    prop_apellidos = models.CharField(max_length=50, blank=True)
    prop_licencia = models.CharField(max_length=100)
    prop_categoria = models.CharField(max_length=20)
    prop_fecha_revalidacion = models.DateField()
    
    def __str__(self):
        return self.prop_nombre

class Vehicule(models.Model):
    veh_id = models.SmallAutoField(primary_key=True)
    veh_placa = models.CharField(max_length=50)
    
    veh_propietario = models.ForeignKey('Owner', models.CASCADE, db_column='veh_propietario')
    veh_destino = models.ForeignKey('Destination', models.CASCADE, db_column='veh_destino')
    
    veh_categoria = models.CharField(max_length=3)
    veh_marca = models.CharField(max_length=50)
    veh_modelo = models.CharField(max_length=50)
    veh_anio_fabricacion = models.IntegerField()
    veh_nro_asientos = models.IntegerField()
    #veh_owner = models.CharField(max_length=50)

    def __str__(self):
        return self.veh_placa

class Ticket(models.Model):
    tic_id = models.SmallAutoField(primary_key=True)
    tic_fecha = models.DateField(default=date.today)
    tic_hora = models.TimeField(default=get_current_time)
    tic_vehiculo = models.ForeignKey('Vehicule', models.DO_NOTHING, db_column='tic_vehiculo')
    tic_tarifa = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='tic_tarifa')
    
    def __str__(self):
        return self.tic_vehiculo.veh_placa
    
class Tarifa(models.Model):
    tar_id = models.SmallAutoField(primary_key=True)
    tar_tarifa = models.IntegerField()
    tar_nro_asientos = models.IntegerField()
    tar_categoria = models.CharField(max_length=3)
    tar_destino = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tar_categoria
    
class Destination(models.Model):
    des_id = models.SmallAutoField(primary_key=True)
    des_nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.des_nombre

class Role(models.Model):
    role_id = models.SmallAutoField(primary_key=True)
    role_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.role_name
      
class User(models.Model):
    user_id = models.SmallAutoField(primary_key=True)
    user_nombre = models.CharField(max_length=20)
    user_apellidos = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)
    user_password = models.CharField(max_length=20)
    user_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='user_role', default=1)
    
    def __str__(self):
        return self.user_nombre