from django.shortcuts import render
from .models import Task

# Create your views here.
# home
def index(request):
    return render(request, '../index.html')

# create_task_view
# read_task_view
# update_task_view
# delete_task_view