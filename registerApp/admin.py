from django.contrib import admin

from .models import Vehicle, Plate, Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'family_name', 'nationalCode', 'phone', 'img', 'description')
    list_filter = ('nationalCode',)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'plate', 'img', 'color', 'type')


class PlateAdmin(admin.ModelAdmin):
    list_display = ('plate_type', 'firstNum', 'alpha', 'secondNum', 'cityNum')
    list_filter = ('plate_type','cityNum','alpha')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Plate, PlateAdmin)
admin.site.register(Owner, OwnerAdmin)
