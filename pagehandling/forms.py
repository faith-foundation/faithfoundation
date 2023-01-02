from django import forms
from .models import eventForm

class Event(forms.ModelForm):
    class Meta:
        model = eventForm
        fields = "__all__"