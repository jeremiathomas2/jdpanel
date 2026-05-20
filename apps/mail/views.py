from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmailAccount, EmailForwarder, AutoResponder, SpamFilter
from apps.websites.models import Website
from apps.services.mail_service import MailService

@login_required
def mail_list(request):
    accounts = EmailAccount.objects.filter(user=request.user)
    forwarders = EmailForwarder.objects.filter(website__user=request.user)
    return render(request, 'mail/list.html', {
        'accounts': accounts,
        'forwarders': forwarders
    })

@login_required
def account_create(request):
    if request.method == 'POST':
        email_prefix = request.POST.get('email_prefix')
        domain_id = request.POST.get('website')
        password = request.POST.get('password')
        quota = request.POST.get('quota', 512)
        
        website = Website.objects.get(pk=domain_id, user=request.user)
        full_email = f"{email_prefix}@{website.domain}"
        
        if MailService.create_email_account(full_email, password, quota):
            EmailAccount.objects.create(
                email=full_email,
                password=password,
                website=website,
                user=request.user,
                quota=quota
            )
            messages.success(request, f"Email account {full_email} created!")
            return redirect('mail:list')
        else:
            messages.error(request, "Failed to create email account on system.")
            
    websites = Website.objects.filter(user=request.user)
    return render(request, 'mail/create.html', {'websites': websites})

@login_required
def auto_responders(request):
    responders = AutoResponder.objects.filter(email_account__user=request.user)
    return render(request, 'mail/auto_responders.html', {'responders': responders})

@login_required
def spam_filters(request):
    filters = SpamFilter.objects.filter(website__user=request.user)
    return render(request, 'mail/spam_filters.html', {'filters': filters})

@login_required
def dkim_spf(request):
    websites = Website.objects.filter(user=request.user)
    return render(request, 'mail/dkim_spf.html', {'websites': websites})
