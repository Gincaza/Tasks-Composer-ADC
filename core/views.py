from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Task

def dashboard(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def tasks(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        if task_id:  # Editar tarefa existente
            task = Task.objects.get(id=task_id)
            task.title = title
            task.description = description
            task.due_date = due_date
            task.save()
        elif title and due_date:  # Criar nova tarefa
            Task.objects.create(title=title, description=description, due_date=due_date)

        return redirect('tasks')

    tasks_list = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks_list})

def rewards(request):
    return render(request, 'rewards.html')

def settings(request):
    return render(request, 'settings.html')
