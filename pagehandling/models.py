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

class Banner(models.Model):
    title = models.CharField('Event Title', max_length=80)
    description = models.TextField('Description', max_length=300)
    banner_image = models.CharField(max_length=2500)

    def __str__(self):
        return self.title

class LandingEvent(models.Model):
    title = models.CharField('Event Name', max_length=80)
    date = models.DateTimeField('Event Date')
    description = models.TextField('Description', max_length=70)
    notification = models.CharField('Notification', max_length=10)
    banner_image = models.CharField(max_length=2500)

    def __str__(self):
        return self.title

class Contact(models.Model):
    subject = models.CharField('Subject', max_length=70)
    mobile_number = models.CharField('Mobile Number', max_length=10, primary_key=True)
    message = models.TextField('Message', max_length=500)
