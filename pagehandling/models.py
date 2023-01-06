from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField('Event Name', max_length=150)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=150)
    manager = models.CharField(max_length=150)
    description = models.TextField(max_length=900, blank=True)
    event_image = models.CharField(max_length=2500)

    def __str__(self):
        return self.name