from . import views
from django.urls import path
from django.views.generic import TemplateView
from starplanner.views import BaseView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', BaseView.as_view(template_name="index.html")),
]