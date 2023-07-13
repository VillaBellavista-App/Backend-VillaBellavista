from django.shortcuts import render

from travels_app.models import Owner, Vehicule, Destination

from travels_app.serializers import VehiculesListSerializer, VehiculesCreateSerializer, OwnersListSerializer, DestinationListSerializer

from rest_framework import generics, status

from rest_framework.views import APIView

from rest_framework.response import Response

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
