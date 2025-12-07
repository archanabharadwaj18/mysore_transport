from django.db import models
# Create your models here.
class BusRoute(models.Model):
    route_number = models.CharField(max_length=10)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.route_number}: {self.start_point} → {self.end_point}"

class BusStop(models.Model):
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='stops')
    stop_name = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.stop_name


class Timetable(models.Model):
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='timetables')
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return f"{self.route.route_number} | {self.departure_time}-{self.arrival_time}"
