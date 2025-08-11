from django.contrib import admin

from routes.models import Route


# Register your models here.
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass
