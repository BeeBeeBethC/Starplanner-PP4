from django.urls import path
from . import views


urlpatterns = [
    path('', views.starplanner, name='starplanner'),
    path('planner/', views.starplanner_home, name="planner_home"),
    path('create/', views.create_task, name="create"),
    path('read/', views.read_task, name="read"),
    path('update/', views.update_task, name="update"),
    path('delete/', views.delete_task, name="delete"),
]