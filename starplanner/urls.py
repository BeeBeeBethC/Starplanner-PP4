from . import views
# from accounts.views import accounts
from django.urls import path

urlpatterns = [
    path('', views.starplanner, name='starplanner'),
    # path('planner/', views.planner_home, name='planner_home'),
    # path('accounts/', accounts.views.accounts, name='accounts'),
    # path('safe/', views.SafeView.as_view(), name='protected_logged_in')
]