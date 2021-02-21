from .models import Geolocation
from rest_framework import serializers


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['ip', 'type', 'continent_name', 'country_name', 'region_name', 'city', 'zip', 'latitude', 'longitude']
