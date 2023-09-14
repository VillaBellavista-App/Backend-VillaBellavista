from rest_framework import serializers

from travels_app.models import Owner, Vehicule, Destination, Ticket, Tarifa, User
from rest_framework.exceptions import ValidationError


# ------------- USERS SERIALIZERS -----------------

class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
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

# ------------- TICKET SERIALIZERS -----------------

class TicketListSerializer(serializers.ModelSerializer):
    
    tic_placa = serializers.CharField(read_only = True, source='tic_vehiculo.veh_placa')
    tic_categoria = serializers.CharField(read_only = True, source='tic_vehiculo.veh_categoria')
    tic_propietario = serializers.CharField(read_only = True, source='tic_vehiculo.veh_propietario.prop_nombre')
    tic_destino = serializers.CharField(read_only = True, source='tic_vehiculo.veh_destino.des_nombre')
    tarifa_quantity = serializers.IntegerField(read_only = True, source='tic_tarifa.tar_tarifa')
    
    class Meta:
        model = Ticket
        fields = ['tic_id', 'tic_fecha', 'tic_hora', 'tic_destino', 'tic_propietario',
                  'tic_placa', 'tic_categoria', 'tic_tarifa', 'tarifa_quantity']

class TicketCreateSerializer(serializers.ModelSerializer):

    vehicule_id = serializers.IntegerField(source='tic_vehiculo.veh_id')
    
    class Meta:
        model = Ticket
        fields = ['vehicule_id']
        
class TicketCountSerializer(serializers.Serializer):
    month = serializers.SerializerMethodField()
    ticket_count = serializers.IntegerField()

    def get_month(self, obj):
        # Extraer el número del mes a partir de la fecha
        return obj['month'].month
    
# ------------- TARIFA SERIALIZERS -----------------

class TarifaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarifa
        fields = '__all__'