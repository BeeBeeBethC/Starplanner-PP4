from django.urls import path
from . import views


urlpatterns = [
    path('', views.starplanner, name='starplanner'),
   # path('create/', views.create_task, name="create"),
   # path('read/', views.read_task, name="read"),
   # path('update/<int:task_id>/', views.update_task, name="update"),
   # path('delete/<int:task_id>/', views.delete_task, name="delete"),
]