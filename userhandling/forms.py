from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

language_choices = [
    ('Hindi', 'Hindi'),
    ('Marathi', 'Marathi'),
    ('English', 'English'),
]


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget())
    gender = forms.CharField(widget=forms.Select(choices=gender_choices))
    mobile_number = forms.CharField(max_length=12, required=True)
    language_of_choice = forms.CharField(widget=forms.Select(choices=language_choices))
    address = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'mobile_number','date_of_birth', 'password1', 'password2')
        