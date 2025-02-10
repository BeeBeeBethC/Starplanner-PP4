from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.template import loader, RequestContext
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# home - starplanner home view!!
def starplanner(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


