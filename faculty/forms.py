from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Proctor

class FacultyRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Proctor
        fields = ['username','email', 'password1', 'password2']