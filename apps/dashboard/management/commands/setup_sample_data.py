from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.dashboard.models import Website, Database, EmailAccount

class Command(BaseCommand):
    help = 'Setup initial admin account and sample data'

    def handle(self, *args, **options):
        # Create Admin
        username = 'admin@jpanel.cloud'
        password = 'admin@123'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Admin {username} already exists'))

        # Create Sample Websites
        if not Website.objects.exists():
            Website.objects.create(domain='example.com', owner='admin', php_version='8.3', disk_used='1.2 GB', disk_percent=40, ssl_status='active', status='active')
            Website.objects.create(domain='test.cloud', owner='admin', php_version='8.2', disk_used='500 MB', disk_percent=15, ssl_status='active', status='active')
            self.stdout.write(self.style.SUCCESS('Successfully created sample websites'))

        # Create Sample Databases
        if not Database.objects.exists():
            Database.objects.create(name='wp_main', owner='admin', size='250 MB', tables_count=45, charset='utf8mb4')
            Database.objects.create(name='app_db', owner='admin', size='1.2 GB', tables_count=120, charset='utf8mb4')
            self.stdout.write(self.style.SUCCESS('Successfully created sample databases'))

        # Create Sample Emails
        if not EmailAccount.objects.exists():
            EmailAccount.objects.create(email='info@example.com', domain='example.com', quota='2 GB', used='450 MB', used_percent=22, dkim_status='Active', status='Active')
            EmailAccount.objects.create(email='admin@test.cloud', domain='test.cloud', quota='5 GB', used='1.1 GB', used_percent=20, dkim_status='Active', status='Active')
            self.stdout.write(self.style.SUCCESS('Successfully created sample emails'))
