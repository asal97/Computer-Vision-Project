from django.contrib import admin

from .models import SystemUser


class UserAdmin(admin.ModelAdmin):
    ordering = ['date_created']
    list_display = ('user_fullname', 'user', 'phone', 'nationalCode', 'approved', 'date_created')
    list_filter = ('approved','date_created')

    def user_fullname(self, obj):
        return "{}".format(obj.user.get_full_name())


admin.site.site_header = "Plate Detector"
admin.site.register(SystemUser, UserAdmin)
