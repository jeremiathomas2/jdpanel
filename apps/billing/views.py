from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Invoice, Subscription

@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'billing/subscription_list.html', {'subscriptions': subscriptions})

@login_required
def payment_gateway(request):
    return render(request, 'billing/payment_gateway.html')
