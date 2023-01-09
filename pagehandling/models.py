from django.db import models
# Create your models here.

event_choices = (
    ("Spiritual Camp - Winter", "Spiritual Camp - Winter"),
    ("Spiritual Camp - Summer", "Spiritual Camp - Summer"),
    ("Spiritual Camp - Lent", "Spiritual Camp - Winter"),
    ("David - Musical Play", "David - Musical Play"),
    ("Passion of Christ - Play", "Passion of Christ"),
    ("Lent Prayers", "Lent Prayers"),
    ("Revival Meetings", "Revival Meetings"),
    ("Free Medical Checkup Camps", "Free Medical Checkup Camps"),
    ("Carol Singing", "Carol Singing"),
)

family_count = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)

class Event(models.Model):
    name = models.CharField('Event Name', max_length=150)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=150)
    manager = models.CharField(max_length=150)
    description = models.TextField(max_length=900, blank=True)
    event_image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField('Event Title', max_length=80)
    description = models.TextField('Description', max_length=300)
    banner_image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

class LandingEvent(models.Model):
    title = models.CharField('Event Name', max_length=80)
    date = models.DateTimeField('Event Date')
    description = models.TextField('Description', max_length=70)
    notification = models.CharField('Notification', max_length=10)
    banner_image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    subject = models.CharField('Subject', max_length=70)
    mobile_number = models.CharField('Mobile Number', max_length=10, primary_key=True)
    message = models.TextField('Message', max_length=500)

class PhotoAlbumCover(models.Model):
    album_name = models.CharField(max_length=150)
    album_date = models.DateTimeField()
    album_cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.album_name

class EventForm(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=10)
    event = models.CharField(max_length=100, choices=event_choices, default=None)
    count_of_family = models.CharField(max_length=10, choices=family_count, default=None)

    def __str__(self):
        return self.first_name