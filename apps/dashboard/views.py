from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.websites.models import Website
from apps.databases.models import Database
from apps.mail.models import EmailAccount
from apps.monitoring.models import ResourceUsage, ServiceStatus
import psutil
import platform

@login_required
def index(request):
    # Get resource usage (mocking for now or using psutil)
    cpu_usage = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    context = {
        'websites_count': Website.objects.filter(user=request.user).count() if not request.user.is_superuser else Website.objects.count(),
        'databases_count': Database.objects.filter(user=request.user).count() if not request.user.is_superuser else Database.objects.count(),
        'emails_count': EmailAccount.objects.filter(user=request.user).count() if not request.user.is_superuser else EmailAccount.objects.count(),
        'cpu_usage': cpu_usage,
        'ram_usage': ram.percent,
        'disk_usage': disk.percent,
        'uptime': "2 days, 4 hours", # Mocked
        'os_info': f"{platform.system()} {platform.release()}",
        'services': ServiceStatus.objects.all(),
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def websites_list(request):
    if request.user.is_superuser:
        websites = Website.objects.all()
    else:
        websites = Website.objects.filter(user=request.user)
    return render(request, 'dashboard/websites.html', {'websites': websites})

@login_required
def databases_list(request):
    if request.user.is_superuser:
        databases = Database.objects.all()
    else:
        databases = Database.objects.filter(user=request.user)
    return render(request, 'dashboard/databases.html', {'databases': databases})

@login_required
def emails_list(request):
    if request.user.is_superuser:
        emails = EmailAccount.objects.all()
    else:
        emails = EmailAccount.objects.filter(user=request.user)
    return render(request, 'dashboard/emails.html', {'emails': emails})
