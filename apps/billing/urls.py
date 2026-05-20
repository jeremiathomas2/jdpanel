from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('payment-gateway/', views.payment_gateway, name='payment_gateway'),
]
