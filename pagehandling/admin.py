from django.contrib import admin
from .models import Event, Contact, LandingEvent, Banner, PhotoAlbum, EventForm
# Register your models here.
admin.site.register([Event, Contact, LandingEvent, Banner, PhotoAlbum, EventForm])