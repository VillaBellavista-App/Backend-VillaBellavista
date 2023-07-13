from django.urls import path, include

from travels_app import views

urlpatterns = [
    
    #------ VEHICULES URLs ------#
    path('vehicules/list', views.VehiculesList.as_view(), name='vehicule-list'),
    path('vehicules/<int:pk>', views.VehiculesListDetail.as_view(), name='vehicules-detail'),
    path('vehicules/create', views.VehiculesCreate.as_view(), name='vehicules-create'),
    
    #------ OWNERS URLs ------#
    path('owners/list', views.OwnersList.as_view(), name='owners-list'),
    path('owners/<int:pk>', views.OwnersListDetail.as_view(), name='owners-detail'),
    path('owners/create', views.OwnersCreate.as_view(), name='owners-create'),
    
     #------ DESTINATION URLs ------#
    path('destination/list', views.DestinationList.as_view(), name='destination-list'),
    path('destination/<int:pk>', views.DestinationDestroy.as_view(), name='destination-detail'),
    path('destination/create', views.DestinationCreate.as_view(), name='destination-create'),
]
