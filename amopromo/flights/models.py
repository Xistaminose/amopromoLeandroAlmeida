from django.db import models


class flight(models.Model):
    urlapi = models.URLField(max_length=200)
    distance = models.FloatField()
    price = models.FloatField()
    aircraft = models.CharField(max_length=64)
    departure = models.CharField(max_length = 4)
    arrival = models.CharField(max_length = 4)
    time = models.CharField(max_length = 9)


