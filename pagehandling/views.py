from django.shortcuts import render
from django.contrib import messages
from .models import Event, LandingEvent, Banner
from .forms import contact_form
from django.views.generic import TemplateView
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

# def landing_events(request):
#     landing_list = LandingEvent.objects.all()
#     return render(request, 'index.html', {'landing_list':landing_list})


def contact(request):
    context = {}
    form = contact_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Feedback Submitted!')
        form.save()

    context['form'] = form
    return render(request, 'contact.html', context)


