from django.shortcuts import render
from django.contrib import messages
from .forms import Event
# Create your views here.

def home(request):
    return render(request, 'index.html')

def event_form(request):
    context = {}
    form = Event(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Form submission successful!')        
        form.save()

    context['form']= form
    return render(request, 'event_registration.html', context)
