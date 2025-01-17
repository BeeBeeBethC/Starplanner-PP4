from . import views
from django.urls import path

urlpatterns = [
    path('', views.starplanner, name='starplanner'),
    path('planner/', views.planner_home, name='planner_home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('safe/', views.SafeView.as_view(), name='protected_logged_in')
]