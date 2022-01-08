from django.urls import path
from .views import VehicleView, SearchMileageView, UpdateVehicleView

urlpatterns = [
    path('', VehicleView.as_view()),
    path('search/<int:vehicle_id>/<str:date>/', SearchMileageView.as_view()),
    path('update/<int:id>/', UpdateVehicleView.as_view())
]
