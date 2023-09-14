from django.shortcuts import render

from travels_app.models import Owner, Vehicule, Destination, Ticket, Tarifa, User

from travels_app.serializers import VehiculesListSerializer, VehiculesCreateSerializer, OwnersListSerializer, DestinationListSerializer, TicketListSerializer, TarifaListSerializer, UserListSerializer, TicketCreateSerializer, TicketCountSerializer

from rest_framework import generics, status

from rest_framework.response import Response

from django.db.models import Count

from django.db.models.functions import TruncMonth

from datetime import datetime, timedelta

# ------------- USERS SECTION -----------------

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserCreate(generics.ListCreateAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        serializer = UserListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class UserLogin(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
    def get_queryset(self):
        return User.objects.filter(user_email = self.kwargs['email'], user_password = self.kwargs['password'])

# ------------- VEHICULES SECTION -----------------

class VehiculesList(generics.ListAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculesListSerializer

class VehiculesByPlate(generics.ListAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculesListSerializer
     
    def get_queryset(self):
        return Vehicule.objects.filter(veh_placa = self.kwargs['placa'])

class VehiculesListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculesListSerializer
    
class VehiculesCreate(generics.CreateAPIView):
    serializer_class = VehiculesCreateSerializer
    permission_classes = []
    
    def get_queryset(self):
        return Vehicule.objects.all()
        
    def post(self, request):
        print(request.data)
        owner_id = Owner.objects.values('prop_id').get(prop_nombre = request.data['owner_name'])
        dest_id = Destination.objects.values('des_id').get(des_nombre = request.data['destino_name'])

        owner_name = request.data.pop('owner_name')
        destino_name = request.data.pop('destino_name')
            
        request.data['veh_propietario'] = owner_id['prop_id']
        request.data['veh_destino'] = dest_id['des_id']
        
        serializer = VehiculesCreateSerializer(data = request.data) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# ------------- OWNERS SECTION -----------------

class OwnersList(generics.ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnersListSerializer
    
class OwnersListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnersListSerializer

class OwnersCreate(generics.CreateAPIView):
    serializer_class = OwnersListSerializer

    def get_queryset(self):
        return Owner.objects.all()

    def post(self, request):
        serializer = OwnersListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# ------------- DESTINATION SECTION -----------------

class DestinationList(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationListSerializer
    
class DestinationCreate(generics.CreateAPIView):
    serializer_class = DestinationListSerializer
    queryset = Destination.objects.all()

    def post(self, request):
        serializer = DestinationListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DestinationDestroy(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationListSerializer

# ------------- TICKET SECTION -----------------

class TicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer

class TicketCreate(generics.CreateAPIView):
    serializer_class = TicketCreateSerializer
    
    def post(self, request):
        serializer = TicketCreateSerializer(data = request.data)
        
        #print(request.data)
        
        if serializer.is_valid():
            #print(serializer.data)
            self.vehicule_id = serializer.data['vehicule_id']
            data = Vehicule.objects.values('veh_categoria', 'veh_nro_asientos', 'veh_destino').get(veh_id = self.vehicule_id)
    
            dest_name = Destination.objects.values('des_nombre').get(des_id = data['veh_destino'])
            
            tarifa_id = 0
            
            if data['veh_categoria'] == 'M1':
                if dest_name['des_nombre'] == 'Juanjui':
                    tarifa_id = 4 #M1 -- 9 soles -- Juanjui
                else:
                    if data['veh_nro_asientos'] == 4:
                        tarifa_id = 2 #M1 -- 6 soles -- 4 asientos
                    elif data['veh_nro_asientos'] == 6:
                        tarifa_id = 3 #M1 -- 8 soles -- 6 asientos
                    else:
                        print("NO ENTRE A NINGUN CONDICIONAL -- ERROR !!!")
            else:
                tarifa_id = 1 #N1 -- 15 soles
            
            print("Vehicule ID: ", self.vehicule_id)
            print("Tarifa ID: ", tarifa_id)
            
            new_ticket = Ticket(tic_vehiculo_id = self.vehicule_id, tic_tarifa_id = tarifa_id)
            
            print("New Ticket: ", new_ticket)
            
            new_ticket.save()
            
            content = {"The ticket was successfully created"}
            return Response(content, status=status.HTTP_200_OK)
        else:
            raise Response(content, status=status.HTTP_400_BAD_REQUEST)

class TicketListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer

class TicketCount(generics.ListAPIView):
    queryset = Ticket.objects.annotate(month=TruncMonth('tic_fecha')).values('month').annotate(ticket_count=Count('tic_id')).order_by('month')
    serializer_class = TicketCountSerializer

# ------------- TARIFA SECTION -----------------
      
class TarifaList(generics.ListAPIView):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaListSerializer
