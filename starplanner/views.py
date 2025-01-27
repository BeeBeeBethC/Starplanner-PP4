from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.template import loader, RequestContext
from django.views import View
from django.contrib.auth.models import User


# Create your views here.
# home - starplanner home view!!
def starplanner(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


# post login page
def starplanner_home(request):
    template = loader.get_template('planner_home.html')
    return HttpResponse(template.render())


# create_task_view
def create_task(request):
    template = loader.get_template('create_task.html')
    return HttpResponse(template.render())


# read_task_view
def read_task(request):
    template = loader.get_template('read_task.html')
    return HttpResponse(template.render())


# update_task_view
def update_task(request):
    template = loader.get_template('update_task.html')
    return HttpResponse(template.render())


# delete_task_view
def delete_task(request):
    template = loader.get_template('delete_task.html')
    return HttpResponse(template.render())
