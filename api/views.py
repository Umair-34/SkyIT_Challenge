import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .serializer import VehicleSerializer, MileageSerializer
from .models import Vehicle, Mileage


class VehicleView(generics.ListCreateAPIView):
    """
    List and Create View for the vehicle
    """
    queryset = Vehicle.objects.all()  # queryset to list the objects
    serializer_class = VehicleSerializer  # this serializer class used to serialized the data


class UpdateVehicleView(generics.RetrieveUpdateAPIView):
    """
    Retrieve and Update view for Vehicle
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = 'id'  # search vehicle by id which is given in url


class CreateMileageView(generics.CreateAPIView):
    """
    This view, creates the mileage for each vehicle in database everyday
    """
    serializer_class = MileageSerializer
    queryset = Mileage.objects.all()

    def post(self, request, *args, **kwargs):      # post method is overriding to avoid data repetition
        vehicle_id = request.data.get('vehicle')    # get vehicle 'id' from posted data
        object_exist = Mileage.objects.filter(vehicle=vehicle_id, created_at=datetime.date.today()).exists()
        # search again vehicle id an current date, .exists() return true if exist otherwise return false
        if object_exist:
            return Response("Today's data already exist for this vehicle")  # if exist send this response
        else:
            return self.create(request, *args, **kwargs)    # if not exists create the object for current date


class CalculateMileageView(generics.GenericAPIView):
    """
    This View, calculate the mileage covered by vehicle from given date to current date
    """
    serializer_class = MileageSerializer

    def get(self, request, *args, **kwargs):        # overriding get method
        vehicle_id = kwargs.get('vehicle_id', '0')      # getting kwargs from url
        date = kwargs.get('date', '0')
        given_data = get_object_or_404(Mileage, vehicle=vehicle_id, created_at=date)  # get object from db according to
        try:                                                                         # given data
            current_date = datetime.date.today()
            print(current_date)
            current_data = get_object_or_404(Mileage, vehicle=vehicle_id, created_at=current_date)
            # this database query return the mileage object of vehicle for the current date, if current date object is
            # not created yet then this will move toward the previous date.
        except Http404:
            current_date = datetime.date.today() - datetime.timedelta(days=1)
            current_data = get_object_or_404(Mileage, vehicle=vehicle_id, created_at=current_date)
            # this database query return the mileage object of vehicle for the yesterday's date

        mileage = current_data.kilometers - given_data.kilometers   # calculating total mileage covered
        return Response(
            "Distance covered by vehicle '" + f"{current_data.vehicle}" + "' between given " + date + " and " +
            f"{current_date}" + " date is: " + f"{mileage}"
        )   # returning mileage as response
