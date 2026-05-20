from django.db import models
from django.contrib.auth.models import User

class Database(models.Model):
    DB_TYPE_CHOICES = (
        ('mysql', 'MySQL'),
        ('mariadb', 'MariaDB'),
    )
    
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='databases')
    db_type = models.CharField(max_length=20, choices=DB_TYPE_CHOICES, default='mysql')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DatabaseUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255) # Encrypted or just stored for panel use
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='db_users')
    databases = models.ManyToManyField(Database, related_name='assigned_users')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
