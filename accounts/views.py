from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
def accounts_home(request):
    template = loader.get_template('accounts.html')
    return HttpResponse(template.render())

    
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
    

def login_user(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
    if user is not None:
            login(render(request, user))
            return redirect('home')
    else:
            # Return an 'invalid login' error message.
            error = ("Credentials Do Not Exist In The Solar System!")
    return redirect('login')
    

def logout_user(request):
    template = loader.get_template('accounts/logout.html')
    return HttpResponse(template.render())
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('starplanner')