from django.db import models

class Website(models.Model):
    domain = models.CharField(max_length=255)
    owner = models.CharField(max_length=100)
    php_version = models.CharField(max_length=10, default='8.3')
    disk_used = models.CharField(max_length=50)
    disk_percent = models.IntegerField(default=0)
    ssl_status = models.CharField(max_length=20, choices=[('active', 'Active'), ('expiring', 'Expiring'), ('none', 'None')])
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('suspended', 'Suspended')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain

class Database(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    tables_count = models.IntegerField(default=0)
    charset = models.CharField(max_length=50, default='utf8mb4')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EmailAccount(models.Model):
    email = models.EmailField(unique=True)
    domain = models.CharField(max_length=255)
    quota = models.CharField(max_length=50)
    used = models.CharField(max_length=50)
    used_percent = models.IntegerField(default=0)
    dkim_status = models.CharField(max_length=20, default='Active')
    status = models.CharField(max_length=20, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
