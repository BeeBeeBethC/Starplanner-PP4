from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Task, Comment
from .forms import TaskForm, CommentForm


def starplanner(request):
    """Render the starplanner home view."""
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


@login_required
def create_task(request):
    """Create a new task for the logged-in user."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                task = form.save(commit=False)
                task.author = request.user
                task.save()
                messages.success(request, 'Task created successfully!')
            except Exception as e:
                messages.error(request, f'Error creating task: {str(e)}')
            Comment.objects.create(
                task=task,
                author=request.user,
                body=(
                    f"Task created on "
                    f"{task.created_on.strftime('%Y-%m-%d %H:%M:%S')}"
                ),
                approved=True
            )
            return redirect('read')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


@login_required
def comments(request, task_id):
    """Display comments for a specific task."""
    task = get_object_or_404(Task, pk=task_id, author=request.user)
    comments = task.comments.all().order_by('-created_on')
    return render(
        request,
        'comment.html',
        {'task': task, 'comments': comments}
    )


@login_required
def read_task(request):
    """Display list of tasks with pagination."""
    filter_user = request.GET.get('user', 'all')
    if filter_user == 'mine':
        task_list = Task.objects.filter(author=request.user)
    else:
        task_list = Task.objects.all()
    paginator = Paginator(task_list, 3)
    page_number = request.GET.get("page")
    tasks = paginator.get_page(page_number)
    return render(
        request,
        'read_task.html',
        {"tasks": tasks, "current_filter": filter_user}
    )


@login_required
def update_task(request, task_id):
    """Update an existing task."""
    task = get_object_or_404(Task, pk=task_id, author=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            Comment.objects.create(
                task=task,
                author=request.user,
                body=(
                    f"Task updated on "
                    f"{task.updated_on.strftime('%Y-%m-%d %H:%M:%S')}"
                ),
                approved=True
            )
            return redirect('read')
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        'update_task.html',
        {'form': form, 'task': task}
    )


@login_required
def delete_task(request, task_id):
    """Delete an existing task."""
    task = get_object_or_404(Task, pk=task_id, author=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('read')
    return render(request, 'delete_task.html', {'task': task})
