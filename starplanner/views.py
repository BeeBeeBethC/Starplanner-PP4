from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.template import loader, RequestContext
from django.views import View
from django.contrib.auth.models import User
from .forms import TaskForm
from .models import Task

# Create your views here.
# home - starplanner home view!!
def starplanner(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


# post login page - REDIRECT LOGIN PAGE TO PLANNER HOME
def starplanner_home(request):
    template = loader.get_template('planner_home.html')
    return HttpResponse(template.render())


# create_task_view
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create/')
    context = {'form': form}
    return render(request, 'create_task.html', context)


# read_task_view
def read_task(request):
    tasks = Task.objects.all()
    return render(request, 'read_task.html', {'tasks': tasks})


# update_task_view
def update_task(request, task_id):
    task = get_object_or_404(Task, task=task_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('read_task')
    return render(request, 'update_task.html', {'form': form})


# delete_task_view
def delete_task(request, task_id):
    task = get_object_or_404(Task, task=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('read_task')
    return render(request, 'delete_task.html', {'task': task})
