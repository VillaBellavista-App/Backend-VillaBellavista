from django.shortcuts import render

from travels_app.models import Owner, Vehicule, Destination, Ticket, Tarifa, User

from travels_app.serializers import VehiculesListSerializer, VehiculesCreateSerializer, OwnersListSerializer, DestinationListSerializer, TicketListSerializer, TarifaListSerializer, UserListSerializer

from rest_framework import generics, status

from rest_framework.views import APIView

from rest_framework.response import Response

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

class VehiculesListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculesListSerializer

class VehiculesCreate(generics.CreateAPIView):
    serializer_class = VehiculesCreateSerializer

    def get_queryset(self):
        return Vehicule.objects.all()

    def post(self, request):
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
    
    serializer_class = TicketListSerializer

    def post(self, request):
        self.vehicule_id = request.data['vehicule_id']
        data = Vehicule.objects.values('veh_categoria', 'veh_nro_asientos', 'veh_destino').get(veh_id = self.vehicule_id)
        dest_name = Destination.objects.values('des_nombre').get(des_id = data['veh_destino'])
        
        tarifa_id = 0
        
        if data['veh_categoria'] == 'M1':
            if dest_name['des_nombre'] == 'Juanjui':
                tarifa_id = 4 
            else:
                if data['veh_nro_asientos'] == 4:
                    tarifa_id = 2 
                elif data['veh_nro_asientos'] == 6:
                    tarifa_id = 3
                else:
                    print("NO ENTRE A NINGUN CONDICIONAL -- ERROR !!!")
        else:
            tarifa_id = 1

        new_ticket = Ticket(tic_vehiculo_id = self.vehicule_id, tic_tarifa_id = tarifa_id)
        new_ticket.save()
        
        content = {"The ticket was successfully created"}
        return Response(content, status=status.HTTP_200_OK)
        
        #FALTA UN RAISE DE ERROR PARA QUE DEVULEVA HTTP_400_BAD_REQUEST
        
class TarifaList(generics.ListAPIView):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaListSerializer
