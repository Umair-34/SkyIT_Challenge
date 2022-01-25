from django.urls import path
from .views import VehicleView, UpdateVehicleView, CreateMileageView, CalculateMileageView
    # importing views from views.py

urlpatterns = [
    # URLS to access views in browser
    path('vehicle/', VehicleView.as_view()),

    path('updateVehicle/<int:id>/', UpdateVehicleView.as_view()),

    path('createMileage/', CreateMileageView.as_view()),

    path('calculateMileage/<int:vehicle_id>/<str:date>/', CalculateMileageView.as_view())

]
