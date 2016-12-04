from django.contrib import admin

from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ['car', 'manager', 'buyer_name', "buyer_last_name"]
    list_display_links = ['car']

    class Meta:
        model = Contract

admin.site.register(Contract, ContractAdmin)