from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Task, CustomUser
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não coincidem.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

@login_required
def dashboard(request):
    pending_tasks_count = Task.objects.filter(completed=False).count()
    completed_tasks_count = Task.objects.filter(completed=True).count()
    overdue_tasks = Task.objects.filter(completed=False, due_date__lt=timezone.now())
    return render(request, 'dashboard.html', {
        'pending_tasks_count': pending_tasks_count,
        'completed_tasks_count': completed_tasks_count,
        'overdue_tasks': overdue_tasks
    })

@login_required
@csrf_exempt
def tasks(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        if task_id:  # Editar tarefa existente
            task = get_object_or_404(Task, id=task_id, user=request.user)
            task.title = title
            task.description = description
            task.due_date = due_date
            task.save()
        elif title and due_date:  # Criar nova tarefa
            Task.objects.create(title=title, description=description, due_date=due_date, user=request.user)

        return redirect('tasks')

    tasks_list = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks_list})

@login_required
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('tasks')

@login_required
def mark_task_completed(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        data = json.loads(request.body)
        task.completed = data.get('completed', False)
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def update_user_info(request):
    if request.method == 'POST':
        user = request.user
        user.name = request.POST.get('name', user.name)
        user.save()
        messages.success(request, 'Informações atualizadas com sucesso!')
        return redirect('settings')
    return redirect('settings')

def home(request):
    return render(request, 'home.html', {'base_template': 'visitor_base.html'})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'base_template': 'visitor_base.html'})
