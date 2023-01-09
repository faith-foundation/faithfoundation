from django.shortcuts import render
from django.contrib import messages
from .models import Event, LandingEvent, Banner, PhotoAlbumCover
from .forms import contact_form, event_registration_form
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    banner_list = Banner.objects.all()
    landing_event = LandingEvent.objects.all()
    return render(request, 'index.html', {'landing_event':landing_event, 'banner_list':banner_list})


def photos(request):
    return render(request, 'photos.html')

def about(request):
    return render(request, 'about.html')

def event_view(request):
    event_list = Event.objects.all()
    return render(request, 'event-view.html', {'event_list':event_list})

def photo_album_view(request):
    album_list = PhotoAlbumCover.objects.all()
    return render(request, 'photo_album_view.html', {'album_list': album_list})

def contact(request):
    context = {}
    form = contact_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Feedback Submitted!')
        form.save()

    context['form'] = form
    return render(request, 'contact.html', context)

@login_required(login_url='login') #redirect when user is not logged in
def event_form(request):
    context = {}
    form = event_registration_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Form Submitted!')
        form.save()

    context['form'] = form
    return render(request, 'event_registration.html', context)



