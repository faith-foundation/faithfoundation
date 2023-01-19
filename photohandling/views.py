from django.shortcuts import render
from .models import *
from pagehandling.models import LandingEvent,Banner

# Create your views here.
def photo_album_view(request):
    album_list_1 = album_1.objects.all()
    album_list_2 = album_2.objects.all()
    album_list_3 = album_3.objects.all()
    album_list_4 = album_4.objects.all()
    album_list_5 = album_5.objects.all()
    album_list_6 = album_6.objects.all()
    album_list_7 = album_7.objects.all()
    album_list_8 = album_8.objects.all()
    album_list_9 = album_9.objects.all()
    album_list_10 = album_10.objects.all()
    landing_event = LandingEvent.objects.all()
    banner_list = Banner.objects.all()
    return render(request, 'photo_album_view.html', {'album_list_1': album_list_1,'album_list_2': album_list_2, 'album_list_3': album_list_3, 'album_list_4':album_list_4, 'album_list_5':album_list_5, 'album_list_6':album_list_6, 'album_list_7':album_list_7, 'album_list_8':album_list_8, 'album_list_9':album_list_9, 'album_list_10':album_list_10,'landing_event': landing_event, 'banner_list': banner_list})

def photo_joseph(request):
    photo_list = photo_album_1.objects.all()
    return render(request, 'joseph_photos.html', {'photo_list': photo_list})