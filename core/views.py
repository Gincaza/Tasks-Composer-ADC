from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def tasks(request):
    return render(request, 'tasks.html')

def rewards(request):
    return render(request, 'rewards.html')

def settings(request):
    return render(request, 'settings.html')
