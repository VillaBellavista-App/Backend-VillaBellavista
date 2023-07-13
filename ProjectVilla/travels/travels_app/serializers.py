from rest_framework import serializers

from travels_app.models import Owner, Vehicule, Destination

# ------------- VEHICULES SERIALIZERS -----------------

class VehiculesListSerializer(serializers.ModelSerializer):
    
    destino_name = serializers.CharField(read_only = True, source='veh_destino.des_nombre')
    owner_name = serializers.CharField(read_only = True, source='veh_propietario.prop_nombre')
    
    class Meta:
        model = Vehicule
        fields = ['veh_id', 'veh_placa', 'veh_categoria', 
                  'veh_marca', 'veh_modelo', 'veh_anio_fabricacion',
                  'veh_nro_asientos', 'destino_name', 'owner_name']

class VehiculesCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehicule
        fields = '__all__'

# ------------- OWNERS SERIALIZERS -----------------

class OwnersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'
        
# ------------- DESTINATION SERIALIZERS -----------------

class DestinationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = '__all__'
