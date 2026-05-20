from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BackupJob, BackupHistory

@login_required
def backup_manager(request):
    jobs = BackupJob.objects.filter(user=request.user)
    history = BackupHistory.objects.filter(job__user=request.user).order_by('-created_at')[:10]
    return render(request, 'backups/manager.html', {'jobs': jobs, 'history': history})

@login_required
def backup_schedules(request):
    jobs = BackupJob.objects.filter(user=request.user)
    return render(request, 'backups/schedules.html', {'jobs': jobs})

@login_required
def backup_restore(request):
    history = BackupHistory.objects.filter(job__user=request.user, status='success').order_by('-created_at')
    return render(request, 'backups/restore.html', {'history': history})

@login_required
def remote_storage(request):
    return render(request, 'backups/remote_storage.html')
