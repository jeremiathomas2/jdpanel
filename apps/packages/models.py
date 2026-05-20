from django.db import models

class HostingPackage(models.Model):
    name = models.CharField(max_length=100)
    disk_space = models.BigIntegerField(help_text="Disk space in MB")
    bandwidth = models.BigIntegerField(help_text="Bandwidth in MB")
    max_websites = models.IntegerField(default=1)
    max_databases = models.IntegerField(default=1)
    max_emails = models.IntegerField(default=1)
    max_ftp_accounts = models.IntegerField(default=1)
    max_subdomains = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
