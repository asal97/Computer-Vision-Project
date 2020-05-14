from django.contrib import admin

from .models import SystemUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_fullname', 'req_date', 'user', 'phone', 'nationalCode', 'approved')
    list_filter = ('approved',)

    def user_fullname(self, obj):
        return "{}".format(obj.user.get_full_name())

    def req_date(self, obj):
        return "{}".format(obj.user.date_joined)


admin.site.site_header = "Plate Detector"
admin.site.register(SystemUser, UserAdmin)
