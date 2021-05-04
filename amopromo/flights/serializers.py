from rest_framework import serializers
from .models import flight
from airports.models import airports

class flightSerializer(serializers.HyperlinkedModelSerializer):
    arrival = serializers.CharField()
    departure = serializers.CharField()
    class Meta:
        model = flight
        fields = ('__all__')

    def create(self, validated_data):
        arrival = validated_data.pop('arrival')
        departure = validated_data.pop('departure')
        arrival_obj = airports.objects.get(iata=arrival)
        departure_obj = airports.objects.get(iata=departure)

    
        flight_instance = flight.objects.create(**validated_data,arrival=arrival_obj, departure=departure_obj)
        return flight_instance

        
