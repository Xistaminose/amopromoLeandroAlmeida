from django.db import models


class airports(models.Model):
    name = models.CharField(max_length = 64)
    iata = models.CharField(max_length = 4)
    lat = models.FloatField()
    lon = models.FloatField()

# Create your models here.
