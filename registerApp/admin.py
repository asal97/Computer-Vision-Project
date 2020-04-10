from django.contrib import admin

from .models import Vehicle,Plate,Owner
admin.site.register(Vehicle)
admin.site.register(Plate)
admin.site.register(Owner)
