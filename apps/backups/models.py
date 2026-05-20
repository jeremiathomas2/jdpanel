from django.db import models
from django.contrib.auth.models import User
from apps.websites.models import Website

class BackupJob(models.Model):
    FREQUENCY_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )
    
    DESTINATION_CHOICES = (
        ('local', 'Local Storage'),
        ('s3', 'Amazon S3'),
        ('gdrive', 'Google Drive'),
        ('ftp', 'FTP Storage'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backup_jobs')
    website = models.ForeignKey(Website, on_delete=models.SET_NULL, null=True, blank=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='daily')
    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES, default='local')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.frequency} - {self.destination}"

class BackupHistory(models.Model):
    job = models.ForeignKey(BackupJob, on_delete=models.CASCADE, related_name='history')
    filename = models.CharField(max_length=255)
    file_path = models.CharField(max_length=512)
    file_size = models.BigIntegerField() # Bytes
    status = models.CharField(max_length=20, default='success') # success, failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename
