from django.db import models
from .choices import STATUS_TYPE


class Vehicle(models.Model):
    """
    This class represents the Vehicle model in data which has 4 fields,
    id: which is auto-incremented by django
    unit: which is the unique combination of characters for every vehicle
    manufacturer: manufacturer name, maximum number of character which user can enter is 20
    status: status is choice field with maximum 11 characters, choices of status is in choices.py file
    """
    unit = models.CharField(max_length=8, unique=True)
    manufacturer = models.CharField(max_length=20)
    status = models.CharField(max_length=11, choices=STATUS_TYPE)

    def __str__(self):  # This is the string representation of model objects
        return f"{self.unit} {self.manufacturer}"

    def current_mileage(self):  # This function will return the current/recent mileage of the vehicle
        return Mileage.objects.filter(vehicle=self)[:1]


class Mileage(models.Model):
    """
        This class represents the Mileage model in data which has 4 fields,
        id: which is auto-incremented by django
        vehicle: vehicle has one to many relationship from mileage
        kilometers: Positive integer field
        created_at: Date field will store the date of every mileage object when saved.
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='mileage')
    kilometers = models.PositiveIntegerField(verbose_name="mileage")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):      # return the string representation of objects
        return f"{self.kilometers} {self.vehicle.unit}"

    class Meta:
        ordering = ['-created_at']      # order all the mileage objects in descending order according to created_at.
