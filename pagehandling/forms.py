from django import forms
from .models import Contact, EventForm

class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class event_registration_form(forms.ModelForm):
    class Meta:
        model = EventForm
        fields = "__all__"