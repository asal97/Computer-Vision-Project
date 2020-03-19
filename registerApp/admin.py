from django.contrib import admin

from .models import Car,Plate,Owner
admin.site.register(Car)
admin.site.register(Plate)
admin.site.register(Owner)
