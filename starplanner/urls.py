from django.urls import path
from . import views


urlpatterns = [
    path('', views.starplanner, name='starplanner'),
    # needs to go to main path('planner/', views.planner_home, name='planner_home'),
    # needs to go to accounts path('accounts/', accounts.views.accounts, name='accounts'),
    # needs to go to main path('safe/', views.SafeView.as_view(), name='protected_logged_in')
]