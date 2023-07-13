from django.db import models

# Create your models here.

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
    
    veh_propietario = models.ForeignKey('Owner', models.DO_NOTHING, db_column='veh_propietario')
    
    veh_destino = models.ForeignKey('Destination', models.DO_NOTHING, db_column='veh_destino')
    
    veh_categoria = models.CharField(max_length=20)
    veh_marca = models.CharField(max_length=50)
    veh_modelo = models.CharField(max_length=50)
    veh_anio_fabricacion = models.IntegerField()
    veh_nro_asientos = models.IntegerField()
    
    def __str__(self):
        return self.veh_placa
    
class Destination(models.Model):
    des_id = models.SmallAutoField(primary_key=True)
    des_nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.des_nombre