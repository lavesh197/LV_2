from django.db import models
from django.utils import timezone
# Create your models here.
user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
class Busstop(models.Model):
    code = models.CharField(max_length=3)
    place = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.place} ({self.code})"

#class Busses(models.Model):
#    departure_time = models.TimeField()

#    def __str__(self):
#        return f"{self.id} {self.departure} to {self.arrival}"
class Buses(models.Model):
    bus_no = models.CharField(max_length=9)
    arrival = models.ForeignKey(Busstop, on_delete=models.CASCADE, related_name="destination")
    departure = models.ForeignKey(Busstop, on_delete=models.CASCADE, related_name="starting_point")
    departure_time = models.TimeField()

    def __str__(self):
        return f"{self.id} {self.bus_no} {self.departure} to {self.arrival}"
