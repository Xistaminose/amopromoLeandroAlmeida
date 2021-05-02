from django.shortcuts import render
from rest_framework import viewsets

from .serializers import airportSerializer
from .models import airports

class airportViewSet(viewsets.ModelViewSet):
    queryset = airports.objects.all().order_by('iata')
    serializer_class = airportSerializer



# Create your views here.
