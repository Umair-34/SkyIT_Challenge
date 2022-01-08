import datetime

from django.db import models
from .choices import STATUS_TYPE


class Vehicle(models.Model):
    unit = models.CharField(max_length=8, unique=True)
    manufacturer = models.CharField(max_length=20)
    status = models.CharField(max_length=11, choices=STATUS_TYPE)

    def __str__(self):
        return f"{self.unit}  {self.manufacturer}"

    def current_mileage(self):
        return Mileage.objects.filter(vehicle=self, created_at=datetime.date.today())


class Mileage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='mileage')
    kilometers = models.PositiveIntegerField(verbose_name="mileage")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.kilometers} {self.vehicle.unit}"

    class Meta:
        ordering = ['-created_at']
