from django.db import models
from django.db.models import Count


class airports(models.Model):
    name = models.CharField(max_length = 64, blank=False)
    iata = models.CharField(max_length = 4, blank=False, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()
    state = models.CharField(max_length = 4, blank=False, default="state")

    def __str__(self):
        return self.iata

    @staticmethod
    def state_with_most_airports():
        x = airports.objects.values_list('state').annotate(airports_count=Count('state')).order_by('-airports_count')
        return x[0]

# Create your models here.
