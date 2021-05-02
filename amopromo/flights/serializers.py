from rest_framework import serializers

from .models import flight

class flightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flight
        fields = ('urlapi', 'distance', 'price', 'aircraft', 'departure', 'arrival','time')