from . import views
from django.urls import path

urlpatterns = [
    path('', views.starplanner, name='starplanner'),
    path('planner_home', views.planner_home, name='planner_home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('registery', views.registery_view, name='registery'),
    path('safe_planner_view/', views.SafeView.as_view(), name='protected_logged_in')
]