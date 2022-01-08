import datetime

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .serializer import VehicleSerializer, MileageSerializer
from .models import Vehicle, Mileage


# Create your views here.
class VehicleView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class UpdateVehicleView(generics.RetrieveUpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class SearchMileageView(generics.GenericAPIView):
    serializer_class = MileageSerializer

    def get(self, request, *args, **kwargs):
        vehicle_id = kwargs.get('vehicle_id', '0')
        date = kwargs.get('date', '0')
        given_data = get_object_or_404(Mileage, vehicle=vehicle_id, created_at=date)
        current_data = get_object_or_404(Mileage, vehicle=vehicle_id, created_at=datetime.date.today())
        mileage = current_data.kilometers - given_data.kilometers
        return Response(
            "Distance covered between given " + date + " and current " +
            str(datetime.date.today()) + " date is: " + str(mileage)
        )
