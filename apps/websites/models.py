from django.db import models
from django.contrib.auth.models import User

class Website(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('pending', 'Pending'),
    )
    
    domain = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='websites')
    php_version = models.CharField(max_length=10, default='8.3')
    doc_root = models.CharField(max_length=512)
    is_ssl_enabled = models.BooleanField(default=False)
    ssl_cert_path = models.CharField(max_length=512, blank=True, null=True)
    ssl_key_path = models.CharField(max_length=512, blank=True, null=True)
    
    disk_limit = models.BigIntegerField(default=1024) # MB
    disk_used = models.BigIntegerField(default=0)
    bandwidth_limit = models.BigIntegerField(default=10240) # MB
    bandwidth_used = models.BigIntegerField(default=0)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain

class DomainAlias(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='aliases')
    domain = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain
