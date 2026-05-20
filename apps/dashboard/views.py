from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Website, Database, EmailAccount

@login_required
def index(request):
    context = {
        'websites_count': Website.objects.count(),
        'databases_count': Database.objects.count(),
        'emails_count': EmailAccount.objects.count(),
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def websites(request):
    websites_list = Website.objects.all()
    return render(request, 'dashboard/websites.html', {'websites': websites_list})

@login_required
def databases(request):
    databases_list = Database.objects.all()
    return render(request, 'dashboard/databases.html', {'databases': databases_list})

@login_required
def emails(request):
    emails_list = EmailAccount.objects.all()
    return render(request, 'dashboard/emails.html', {'emails': emails_list})
