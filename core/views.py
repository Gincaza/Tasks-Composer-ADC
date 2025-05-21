from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Task

def dashboard(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def tasks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        if title and due_date:
            Task.objects.create(title=title, description=description, due_date=due_date)
            return redirect('tasks')

    tasks_list = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks_list})

def rewards(request):
    return render(request, 'rewards.html')

def settings(request):
    return render(request, 'settings.html')
