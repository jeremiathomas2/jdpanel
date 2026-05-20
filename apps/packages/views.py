from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import HostingPackage

def is_admin(user):
    return user.is_superuser or (hasattr(user, 'profile') and user.profile.role == 'admin')

@login_required
def package_list(request):
    packages = HostingPackage.objects.filter(is_active=True)
    return render(request, 'packages/list.html', {'packages': packages})

@login_required
@user_passes_test(is_admin)
def package_create(request):
    return render(request, 'packages/create.html')
