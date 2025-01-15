from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import path
from django.template import loader

# Create your views here.
# home - starplanner home view!!
def starplanner(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

# create_task_view
# read_task_view
# update_task_view
# delete_task_view