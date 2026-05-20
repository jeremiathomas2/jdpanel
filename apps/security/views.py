from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import FirewallRule, IPBlock

def is_admin(user):
    return user.is_superuser or (hasattr(user, 'profile') and user.profile.role == 'admin')

@login_required
@user_passes_test(is_admin)
def firewall_manager(request):
    rules = FirewallRule.objects.all()
    return render(request, 'security/firewall.html', {'rules': rules})

@login_required
@user_passes_test(is_admin)
def fail2ban_status(request):
    # Mocking status
    jails = [
        {'name': 'sshd', 'status': 'Active', 'failed': 12, 'banned': 2},
        {'name': 'apache-auth', 'status': 'Active', 'failed': 5, 'banned': 0},
    ]
    return render(request, 'security/fail2ban.html', {'jails': jails})

@login_required
@user_passes_test(is_admin)
def malware_scanner(request):
    return render(request, 'security/malware.html')

@login_required
@user_passes_test(is_admin)
def ip_blocking(request):
    blocks = IPBlock.objects.all()
    return render(request, 'security/ip_blocking.html', {'blocks': blocks})

@login_required
@user_passes_test(is_admin)
def modsecurity_config(request):
    return render(request, 'security/modsecurity.html')
