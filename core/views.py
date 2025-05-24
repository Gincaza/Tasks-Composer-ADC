from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Task
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def dashboard(request):
    pending_tasks_count = Task.objects.filter(completed=False).count()
    completed_tasks_count = Task.objects.filter(completed=True).count()
    overdue_tasks = Task.objects.filter(completed=False, due_date__lt=timezone.now())
    return render(request, 'dashboard.html', {
        'pending_tasks_count': pending_tasks_count,
        'completed_tasks_count': completed_tasks_count,
        'overdue_tasks': overdue_tasks
    })

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

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('tasks')

def mark_task_completed(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        data = json.loads(request.body)
        task.completed = data.get('completed', False)
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def settings(request):
    return render(request, 'settings.html')

@login_required
def update_user_info(request):
    if request.method == 'POST':
        user = request.user
        user.name = request.POST.get('name', user.name)
        if 'avatar' in request.FILES:
            user.avatar = request.FILES['avatar']
        user.save()
        messages.success(request, 'Informações atualizadas com sucesso!')
        return redirect('settings')
    return redirect('settings')
