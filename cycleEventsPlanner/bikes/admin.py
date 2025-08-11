from django.contrib import admin

from bikes.models import Bike


# Register your models here.
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    pass
