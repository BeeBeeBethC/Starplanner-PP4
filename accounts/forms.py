from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    register_user = forms.CharField(label="Your Name", max_length=50)

