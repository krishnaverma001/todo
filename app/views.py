from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def update(request, k):
    task = get_object_or_404(Task, id=k)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'update.html', context)

def delete(request, k):
    item = get_object_or_404(Task, id=k)
    if request.method == 'POST':
        item.delete()
        return redirect('index')

    context = {'item': item}
    return render(request, 'delete.html', context)

def toggle(request, k):
    task = get_object_or_404(Task, id=k)
    if request.method == 'POST':
        task.complete = not task.complete
        task.save()

    return redirect('index')
