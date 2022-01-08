from .models import Vehicle, Mileage
from rest_framework import serializers


class MileageSerializer(serializers.ModelSerializer):
    # vehicle = serializers.CharField(source='vehicle.unit')
    # instead of id show vehicle unit number

    class Meta:
        model = Mileage
        fields = ['vehicle', 'kilometers', ]


class VehicleSerializer(serializers.ModelSerializer):
    mileage = MileageSerializer(many=True, source="current_mileage")

    class Meta:
        model = Vehicle
        fields = ['unit', 'manufacturer', 'status', 'mileage']

    # yahan create and update me heinki peinki lga k hoga wo lekin mjhy ye nae smj aa rha

    def create(self, validated_data):
        pass

    # what i think is k is update k function me mileage ka naya object bnanty jayen hr roz, wo json me update kray lekin
    # hm is function me update krnay ki bjaye aik naya object bna dein. Baki jis trha apko bhtr lagy mjhy smjha do.
    def update(self, instance, validated_data):
        pass
