from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    your_username = forms.CharField(label="put your username in here", max_length=50)