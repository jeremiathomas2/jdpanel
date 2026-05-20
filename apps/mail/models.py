from django.db import models
from django.contrib.auth.models import User
from apps.websites.models import Website

class EmailAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='email_accounts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_accounts')
    quota = models.BigIntegerField(default=512) # MB
    quota_used = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class EmailForwarder(models.Model):
    source = models.EmailField()
    destination = models.EmailField()
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='email_forwarders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} -> {self.destination}"

class AutoResponder(models.Model):
    email_account = models.OneToOneField(EmailAccount, on_delete=models.CASCADE, related_name='auto_responder')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Auto Responder for {self.email_account.email}"

class SpamFilter(models.Model):
    website = models.OneToOneField(Website, on_delete=models.CASCADE, related_name='spam_filter')
    threshold = models.IntegerField(default=5) # 1-10
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Spam Filter for {self.website.domain}"
