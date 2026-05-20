from django.urls import path
from . import views

app_name = 'security'

urlpatterns = [
    path('firewall/', views.firewall_manager, name='firewall'),
    path('fail2ban/', views.fail2ban_status, name='fail2ban'),
    path('malware/', views.malware_scanner, name='malware'),
    path('ip-blocking/', views.ip_blocking, name='ip_blocking'),
    path('modsecurity/', views.modsecurity_config, name='modsecurity'),
]
