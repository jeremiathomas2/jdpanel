from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website
from .forms import WebsiteForm
from apps.services.linux_service import LinuxService
from .file_manager_views import file_manager

@login_required
def website_list(request):
    websites = Website.objects.filter(user=request.user)
    return render(request, 'websites/list.html', {'websites': websites})

@login_required
def website_create(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            website.user = request.user
            
            # System automation
            username = request.user.username
            domain = website.domain
            php_version = website.php_version
            
            # 1. Setup directories
            doc_root = LinuxService.setup_website_dirs(username, domain)
            if doc_root:
                website.doc_root = doc_root
                
                # 2. Create Apache VHost
                if LinuxService.create_apache_vhost(username, domain, php_version):
                    website.save()
                    messages.success(request, f"Website {domain} created successfully!")
                    return redirect('websites:list')
                else:
                    messages.error(request, "Failed to create Apache VirtualHost.")
            else:
                messages.error(request, "Failed to setup website directories.")
    else:
        form = WebsiteForm()
    
    return render(request, 'websites/create.html', {'form': form})

@login_required
def website_delete(request, pk):
    website = get_object_or_004(Website, pk=pk, user=request.user)
    if request.method == 'POST':
        # Logic to remove vhost and files could go here
        website.delete()
        messages.success(request, "Website deleted successfully.")
        return redirect('websites:list')
    return render(request, 'websites/delete_confirm.html', {'website': website})
