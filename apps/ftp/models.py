from django.db import models
from django.contrib.auth.models import User
from apps.websites.models import Website

class FTPAccount(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='ftp_accounts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ftp_accounts')
    path = models.CharField(max_length=512)
    quota = models.BigIntegerField(default=0) # 0 for unlimited
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
