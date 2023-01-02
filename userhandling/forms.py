from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    date_of_birth = forms.DateField(required=True)
    mobile_number = forms.CharField(max_length=12, required=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'mobile_number','date_of_birth', 'password1', 'password2')
        