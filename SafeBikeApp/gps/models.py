from django.db import models
from .observable import Observable
from django.shortcuts import render
class RecordedValue(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField()
    interval = models.IntegerField(default=0)  # Add an interval field

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.date} - {self.interval} minute interval"

    