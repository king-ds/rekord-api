from django.db import models

# Models for transportation
class Transportation(models.Model):
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cost = models.IntegerField()
    departure_date = models.DateTimeField()
    eta = models.IntegerField()
    vehicle_type = models.CharField(max_length=20)
    arrived = models.BooleanField(default=False)
    arrival_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.location