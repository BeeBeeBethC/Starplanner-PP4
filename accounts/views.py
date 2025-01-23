from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.view import View
from django.contrib.auth.models import User

# Create your views here.
def new_user(request):
    return render(request, 'accounts/register.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            error = ("Credentials Do Not Exist In The Solar System!")
            return redirect('login_user')
    else:
        return render(request, 'accounts/login.html', {})

def logout_user(request):
    template = loader.get_template('accounts/logout.html')
    return HttpResponse(template.render())
    if request.method == "POST":
        logout(request)
        return redirect('login_user')
    else:
        return redirect('starplanner')