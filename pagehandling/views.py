from django.shortcuts import render
from django.contrib import messages
from .models import Event
# Create your views here.

def home(request):
    return render(request, 'index.html')

def photos(request):
    return render(request, 'photos.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def event_view(request):
    event_list = Event.objects.all()
    return render(request, 'event-view.html', {'event_list':event_list})

# def event_form(request):
#     context = {}
#     form = Event(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         messages.success(request, 'Form submission successful!')
#         form.save()
#
#     context['form']= form
#     return render(request, 'event_registration.html', context)
