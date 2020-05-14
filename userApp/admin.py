from django.contrib import admin

from .models import SystemUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('user','phone','nationalCode','approved')





admin.site.site_header = "Plate Detector"
admin.site.register(SystemUser,UserAdmin)
