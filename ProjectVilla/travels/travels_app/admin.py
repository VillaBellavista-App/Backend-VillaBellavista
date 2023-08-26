from django.contrib import admin
from travels_app.models import Owner, Vehicule, Destination, Ticket, Tarifa, User, Role

# Register your models here.

admin.site.register(Owner)
admin.site.register(Vehicule)
admin.site.register(Destination)
admin.site.register(Ticket)
admin.site.register(Tarifa)
admin.site.register(User)
admin.site.register(Role)