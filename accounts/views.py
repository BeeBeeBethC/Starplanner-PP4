from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def accounts(request):
    template = loader.get_template('accounts/register.html')
    return HttpResponse(template.render())