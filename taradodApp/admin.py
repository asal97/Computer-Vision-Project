from django.contrib import admin

# Register your models here.


from .models import Taradod


class TaradodAdmin(admin.ModelAdmin):
    ordering = ['seen']
    list_display_links = ['plate']
    list_display = ('plate','img', 'seen', 'approved')
    list_filter = ('approved', 'seen')


admin.site.register(Taradod, TaradodAdmin)
