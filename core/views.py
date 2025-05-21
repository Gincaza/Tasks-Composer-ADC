from django.shortcuts import render
from .models import Task

def dashboard(request):
    return render(request, 'dashboard.html')

def tasks(request):
    tasks_list = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks_list})

def rewards(request):
    return render(request, 'rewards.html')

def settings(request):
    return render(request, 'settings.html')
