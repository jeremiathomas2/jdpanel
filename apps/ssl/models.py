from django.db import models
from apps.websites.models import Website

class SSLCertificate(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='ssl_certificates')
    provider = models.CharField(max_length=100, default="Let's Encrypt")
    certificate = models.TextField()
    private_key = models.TextField()
    chain = models.TextField(blank=True, null=True)
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    auto_renew = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SSL for {self.website.domain}"
