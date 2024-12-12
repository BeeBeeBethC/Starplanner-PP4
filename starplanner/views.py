from django.shortcuts import render
from django.views.generic import TemplateView
# from .models import Post


# Create your views here.
def home(request):
    return render(request,'base.html')

class BaseView(TemplateView):
    template_name = "index.html"