from rest_framework import serializers

from .models import airports

class airportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = airports
        fields = ('name', 'iata', 'lat', 'lon')