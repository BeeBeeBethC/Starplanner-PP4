from django.urls import path
from . import views


urlpatterns = [
    path('', views.accounts_home, name='accounts'),
    path('login/', views.login_user, name='login'),
    path('register', views.register, name="register"),
]