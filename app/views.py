from django.shortcuts import render, redirect
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


def update(request, k):
    task = Task.objects.get(id=k)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'form': form}
    return render(request, 'update.html', context)

def delete(request, k):
    item = Task.objects.get(id=k)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)

def toggle(request, k):
    task = Task.objects.get(id=k)

    if request.method == 'POST':
        task.complete = not task.complete
        task.save()

    return redirect('/')