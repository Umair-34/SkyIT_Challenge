from django.contrib import admin
from .models import Vehicle, Mileage


class MileageAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'kilometers', 'created_at')


admin.site.register(Vehicle)
admin.site.register(Mileage, MileageAdmin)
