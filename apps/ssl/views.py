from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SSLCertificate
from apps.websites.models import Website

@login_required
def certificate_list(request):
    certificates = SSLCertificate.objects.filter(website__user=request.user)
    return render(request, 'ssl/list.html', {'certificates': certificates})

@login_required
def auto_install(request):
    websites = Website.objects.filter(user=request.user, is_ssl_enabled=False)
    return render(request, 'ssl/auto_install.html', {'websites': websites})

@login_required
def custom_upload(request):
    websites = Website.objects.filter(user=request.user)
    return render(request, 'ssl/custom_upload.html', {'websites': websites})
