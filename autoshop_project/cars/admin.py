from django.contrib import admin

from .models import Car, CarColor, CarState
# Register your models here.
admin.site.register(Car)
admin.site.register(CarState)
admin.site.register(CarColor)

