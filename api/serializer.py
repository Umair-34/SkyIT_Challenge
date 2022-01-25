from .models import Vehicle, Mileage        # importing models from models.py file
from rest_framework import serializers      # importing serializers from rest_framework


class MileageSerializer(serializers.ModelSerializer):
    """
    This serializer class is for Mileage model
    """

    class Meta:
        model = Mileage
        fields = ['vehicle', 'kilometers']
        # fields that user enters in frontend(Json format) and then should be converted to internal datatype


class VehicleSerializer(serializers.ModelSerializer):
    """
       This serializer class is for Vehicle model
    """
    mileage = MileageSerializer(many=True, source="current_mileage", read_only=True)

    # mileage field is added to vehicle serializer to show the mileage of every vehicle in List View(nested serializer)

    class Meta:
        model = Vehicle
        fields = ['id', 'unit', 'manufacturer', 'status', 'mileage']
