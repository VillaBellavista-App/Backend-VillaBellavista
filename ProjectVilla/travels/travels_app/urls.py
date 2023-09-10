from django.urls import path, include

from travels_app import views

from django.db.models import Count
from datetime import datetime

urlpatterns = [
    
    #------ USER URLs ------#
    path('user/list', views.UserList.as_view(), name='user-list'),
    path('user/create', views.UserCreate.as_view(), name='user-create'),
    path('user/authenticate/<str:email>/<str:password>', views.UserLogin.as_view(), name='user-login'),
    
    #------ VEHICULES URLs ------#
    path('vehicules/list', views.VehiculesList.as_view(), name='vehicule-list'),
    path('vehicules/<int:pk>', views.VehiculesListDetail.as_view(), name='vehicules-detail'),
    path('vehicules/create', views.VehiculesCreate.as_view(), name='vehicules-create'),
    path('vehicules/plate/<str:placa>', views.VehiculesByPlate.as_view(), name='vehicules-plate'),
    
    #------ OWNERS URLs ------#
    path('owners/list', views.OwnersList.as_view(), name='owners-list'),
    path('owners/<int:pk>', views.OwnersListDetail.as_view(), name='owners-detail'),
    path('owners/create', views.OwnersCreate.as_view(), name='owners-create'),
    
     #------ DESTINATION URLs ------#
    path('destination/list', views.DestinationList.as_view(), name='destination-list'),
    path('destination/<int:pk>', views.DestinationDestroy.as_view(), name='destination-delete'),
    path('destination/create', views.DestinationCreate.as_view(), name='destination-create'),

    #------ TICKET URLs ------#
    path('ticket/list', views.TicketList.as_view(), name='ticket-list'),
    path('ticket/<int:pk>', views.TicketListDetail.as_view(), name='ticket-detail'),
    path('ticket/create', views.TicketCreate.as_view(), name='ticket-create'),
    path('ticket/count', views.TicketCountMonth.as_view(), name='ticket-count'),
    
    #------ TARIFA URLs ------#
    path('tarifa/list', views.TarifaList.as_view(), name='tarifa-list'),
]
