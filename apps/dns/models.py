from django.db import models
from django.contrib.auth.models import User

class DNSZone(models.Model):
    domain = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dns_zones')
    ttl = models.IntegerField(default=3600)
    retry = models.IntegerField(default=3600)
    refresh = models.IntegerField(default=86400)
    expire = models.IntegerField(default=2419200)
    minimum = models.IntegerField(default=3600)
    serial = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain

class DNSRecord(models.Model):
    RECORD_TYPES = (
        ('A', 'A'),
        ('AAAA', 'AAAA'),
        ('CNAME', 'CNAME'),
        ('MX', 'MX'),
        ('TXT', 'TXT'),
        ('NS', 'NS'),
        ('SRV', 'SRV'),
        ('CAA', 'CAA'),
    )
    
    zone = models.ForeignKey(DNSZone, on_delete=models.CASCADE, related_name='records')
    name = models.CharField(max_length=255) # e.g., @, www, mail
    type = models.CharField(max_length=10, choices=RECORD_TYPES)
    value = models.CharField(max_length=512)
    priority = models.IntegerField(default=0, null=True, blank=True)
    ttl = models.IntegerField(default=3600)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.type} {self.value}"
