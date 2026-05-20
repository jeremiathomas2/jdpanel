from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DNSZone, DNSRecord

@login_required
def zone_list(request):
    zones = DNSZone.objects.filter(user=request.user)
    return render(request, 'dns/zone_list.html', {'zones': zones})

@login_required
def record_list(request, zone_id):
    zone = get_object_or_404(DNSZone, pk=zone_id, user=request.user)
    records = zone.records.all()
    return render(request, 'dns/record_list.html', {'zone': zone, 'records': records})

@login_required
def propagation_check(request):
    zones = DNSZone.objects.filter(user=request.user)
    return render(request, 'dns/propagation_check.html', {'zones': zones})
