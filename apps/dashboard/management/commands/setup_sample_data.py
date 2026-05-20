from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.accounts.models import UserProfile
from apps.websites.models import Website
from apps.databases.models import Database
from apps.mail.models import EmailAccount
from apps.monitoring.models import ServiceStatus
from apps.packages.models import HostingPackage

class Command(BaseCommand):
    help = 'Setup initial admin account and sample data'

    def handle(self, *args, **options):
        # Create Package
        package, _ = HostingPackage.objects.get_or_create(
            name='Premium Plan',
            disk_space=51200,
            bandwidth=102400,
            max_websites=10,
            max_databases=10,
            max_emails=50
        )

        # Create Admin
        username = 'admin'
        password = 'admin123'
        user, created = User.objects.get_or_create(username=username, defaults={'email': 'admin@jdpanel.io'})
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin: {username}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Successfully updated admin: {username}'))
        
        profile, _ = UserProfile.objects.get_or_create(user=user, defaults={'role': 'admin', 'package': package})

        # Create Sample Websites
        if not Website.objects.exists():
            Website.objects.create(domain='example.com', user=user, php_version='8.3', disk_used=1200, disk_limit=5000)
            Website.objects.create(domain='test.cloud', user=user, php_version='8.2', disk_used=500, disk_limit=5000)
            self.stdout.write(self.style.SUCCESS('Successfully created sample websites'))

        # Create Sample Databases
        if not Database.objects.exists():
            Database.objects.create(name='wp_main', user=user, db_type='mysql')
            Database.objects.create(name='app_db', user=user, db_type='mariadb')
            self.stdout.write(self.style.SUCCESS('Successfully created sample databases'))

        # Create Sample Emails
        if not EmailAccount.objects.exists():
            site = Website.objects.first()
            EmailAccount.objects.create(email='info@example.com', website=site, user=user, quota=2048, quota_used=450)
            self.stdout.write(self.style.SUCCESS('Successfully created sample emails'))

        # Create Services
        services = ['Apache', 'MySQL', 'Redis', 'Postfix', 'Dovecot', 'BIND9', 'Pure-FTPd', 'Fail2Ban', 'Celery']
        for s in services:
            ServiceStatus.objects.get_or_create(name=s, defaults={'is_running': True})
        self.stdout.write(self.style.SUCCESS('Successfully created sample services'))
