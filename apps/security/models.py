from django.db import models
from django.contrib.auth.models import User

class FirewallRule(models.Model):
    ACTION_CHOICES = (
        ('ALLOW', 'Allow'),
        ('DENY', 'Deny'),
    )
    
    PROTOCOL_CHOICES = (
        ('TCP', 'TCP'),
        ('UDP', 'UDP'),
        ('BOTH', 'Both'),
    )
    
    name = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=10, choices=PROTOCOL_CHOICES, default='TCP')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, default='ALLOW')
    source_ip = models.GenericIPAddressField(null=True, blank=True, help_text="Leave blank for any IP")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.port}/{self.protocol}) - {self.action}"

class IPBlock(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    blocked_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.ip_address
