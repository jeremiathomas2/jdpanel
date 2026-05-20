from django.db import models
from django.contrib.auth.models import User
from apps.packages.models import HostingPackage

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Super Administrator'),
        ('reseller', 'Reseller'),
        ('user', 'Hosting User'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    package = models.ForeignKey(HostingPackage, on_delete=models.SET_NULL, null=True, blank=True)
    reseller = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')
    two_factor_enabled = models.BooleanField(default=False)
    two_factor_secret = models.CharField(max_length=32, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.role})"
