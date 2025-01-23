from django.urls import path
from . import views


urlpatterns = [
    path('new_user', views.new_user, name="register"),
]