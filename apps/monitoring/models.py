from django.db import models

class ResourceUsage(models.Model):
    cpu_usage = models.FloatField() # Percentage
    ram_usage = models.FloatField() # Percentage
    disk_usage = models.FloatField() # Percentage
    load_average = models.CharField(max_length=50) # e.g., "0.5, 0.7, 0.8"
    uptime = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usage at {self.timestamp}"

class ServiceStatus(models.Model):
    name = models.CharField(max_length=100, unique=True) # e.g., Apache, MySQL, Postfix
    is_running = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {'Running' if self.is_running else 'Stopped'}"
