from django.db import models

class RecordedValue(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.date}"
