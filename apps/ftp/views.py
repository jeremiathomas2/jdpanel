from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FTPAccount

@login_required
def account_list(request):
    accounts = FTPAccount.objects.filter(user=request.user)
    return render(request, 'ftp/list.html', {'accounts': accounts})

@login_required
def ftp_logs(request):
    # Mocking logs for now
    logs = [
        {'time': '2024-05-20 10:00:01', 'user': 'ftp_user1', 'action': 'Login', 'status': 'Success', 'ip': '1.2.3.4'},
        {'time': '2024-05-20 10:05:22', 'user': 'ftp_user1', 'action': 'Upload', 'file': 'index.html', 'ip': '1.2.3.4'},
    ]
    return render(request, 'ftp/logs.html', {'logs': logs})
