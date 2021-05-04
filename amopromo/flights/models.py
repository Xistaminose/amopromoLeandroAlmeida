from django.db import models
from airports.models import airports

class flight(models.Model):
    urlapi = models.URLField(max_length=200, unique=True)
    distance = models.FloatField()
    price = models.FloatField()
    aircraft = models.CharField(max_length=64)
    departure = models.ForeignKey(airports, on_delete = models.CASCADE, related_name='departure')
    arrival = models.ForeignKey(airports, on_delete = models.CASCADE, related_name='arrival')
    time = models.IntegerField()

    def __str__(self):
        return "{} to {}".format(self.departure, self.arrival)

    @staticmethod
    def get_top_n_time(n):
        top_scores = flight.objects.order_by('-time')[:n]
        return top_scores
