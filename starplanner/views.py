from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.template import loader, RequestContext
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


# home - starplanner home view!!
def starplanner(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


# create_task_view
@login_required
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
@login_required
def read_task(request):
    tasks = Task.objects.all()
    return render(request, 'read_task.html', {'tasks': tasks})


# update_task_view
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, task=task_id)
    form = TaskForm(request.POST, instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('read_task')
        else:
            form=TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, 'task': task})


# delete_task_view
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, task=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('read_task')
    return render(request, 'delete_task.html', {'task': task})
