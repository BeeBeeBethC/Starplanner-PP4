from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, CommentForm

# home - starplanner home view!!
def starplanner(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('read_task')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


@login_required
def read_task(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, pk=task_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('read_task')
    else:
        comment_form = CommentForm()
    return render(request, 'read_task.html', {
        'tasks': tasks,
        'comment_form': comment_form,
    })


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, task=task_id, author=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('read_task')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, 'task': task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, task=task_id, author=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('read_task')
    return render(request, 'delete_task.html', {'task': task})