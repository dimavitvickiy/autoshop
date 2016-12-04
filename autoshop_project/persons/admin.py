from django.contrib import admin
from .models import *


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['autoshop', 'account', 'passport']
    list_display_links = ['passport']

    class  Meta:
        model = Manager


admin.site.register(Manager, ManagerAdmin)
