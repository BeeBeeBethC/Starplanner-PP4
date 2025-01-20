from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm


# Create your views here.
# home - starplanner home view!!
def starplanner(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

# create_task_view
# read_task_view
# update_task_view
# delete_task_view


# create user view
def register_view(request):
    template = loader.get_template('accounts/register.html')
    return HttpResponse(template.render())
    if request.method == "POST":
        request_context = RequestContext(request)
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.object.create_user(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("login/")
    else:
            form = RegisterForm()
    return render(request, 'accounts/register.html', {"form": form})


def login_view(request):
    template = loader.get_template('accounts/login.html')
    return HttpResponse(template.render())
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            request.POST.get('next') or request.GET.get('next') or 'starplanner'
            return redirect(next_url)
    else:
        error_message = "Credentials Do Not Exist In The Solar System!"
    return render(request, 'accounts/login.html', {'error' :error_message})


def logout_view(request):
    template = loader.get_template('accounts/logout.html')
    return HttpResponse(template.render())
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('starplanner')


# logged in view
# using login required decorator
@login_required
def planner_home(request):
    return render(request, 'accounts/safe_planner_view.html')

class SafeView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'accounts/safe_planner_view.html')