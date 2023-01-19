from django.shortcuts import render
from django.contrib import messages
from .models import Event, LandingEvent, Banner
from .forms import contact_form, event_registration_form
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    banner_list = Banner.objects.all()
    landing_event = LandingEvent.objects.all()
    return render(request, 'index.html', {'landing_event': landing_event, 'banner_list': banner_list})


def photos(request):
    landing_event = LandingEvent.objects.all()
    return render(request, 'photos.html', {'landing_event': landing_event})


def about(request):
    landing_event = LandingEvent.objects.all()
    return render(request, 'about.html',{'landing_event': landing_event})


def event_view(request):
    banner_list = Banner.objects.all()
    event_list = Event.objects.all()
    landing_event = LandingEvent.objects.all()
    return render(request, 'event-view.html', {'event_list': event_list,'banner_list': banner_list,'landing_event': landing_event})

def event_Reg(request):
    banner_list = Banner.objects.all()
    event_list = Event.objects.all()
    return render(request, 'event_registration.html', {'event_list': event_list,'banner_list': banner_list,})

def contact(request):
    landing_event = LandingEvent.objects.all()
    context = {}
    form = contact_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Feedback Submitted!')
        form.save()

    context['form'] = form
    return render(request, 'contact.html',{'context':context,'landing_event': landing_event})


@login_required(login_url='login')  # redirect when user is not logged in
def event_form(request):
    landing_event = LandingEvent.objects.all()
    context = {}
    form = event_registration_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Form Submitted!')
        form.save()

    context['form'] = form
    return render(request, 'event_registration.html',{'landing_event': landing_event ,'context': context })
