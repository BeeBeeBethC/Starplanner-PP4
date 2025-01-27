from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.
def accounts_home(request):
    template = loader.get_template('accounts.html')
    return HttpResponse(template.render())

    
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
    

def login_user(request):
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(render(request, user))
                return redirect('home')
            else:
                error = ("Credentials Do Not Exist In The Solar System!")
                return redirect('login')
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render())


def logout_user(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('starplanner')