from . import views
from django.urls import path

urlpatterns = [
    path('', views.starplanner, name='starplanner'),
    path('planner/', views.planner_home, name='planner_home'),
    path('accounts/', views.accounts, name='accounts'),
    path('safe/', views.SafeView.as_view(), name='protected_logged_in')
]