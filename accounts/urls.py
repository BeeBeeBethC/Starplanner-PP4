from django.urls import path
from . import views


urlpatterns = [
    path('', views.accounts_home, name='accounts'),
    path('login/', views.login_user, name='login'),
    # path('new_user', views.new_user, name="register"),
]