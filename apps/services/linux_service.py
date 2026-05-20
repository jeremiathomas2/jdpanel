import os
import subprocess
import platform

class LinuxService:
    @staticmethod
    def is_linux():
        return platform.system() == "Linux"

    @staticmethod
    def create_user(username):
        if not LinuxService.is_linux():
            print(f"Mock: Creating user {username}")
            return True
        try:
            subprocess.run(['useradd', '-m', '-s', '/bin/bash', username], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def setup_website_dirs(username, domain):
        base_path = f"/home/{username}/{domain}"
        dirs = ['public_html', 'logs', 'backups', 'mail']
        
        if not LinuxService.is_linux():
            print(f"Mock: Setting up dirs for {domain} under {username}")
            return base_path

        try:
            os.makedirs(base_path, exist_ok=True)
            for d in dirs:
                os.makedirs(os.path.join(base_path, d), exist_ok=True)
            
            # Set permissions
            subprocess.run(['chown', '-R', f'{username}:{username}', base_path], check=True)
            return base_path
        except Exception as e:
            print(f"Error setting up dirs: {e}")
            return None

    @staticmethod
    def create_apache_vhost(username, domain, php_version):
        vhost_config = f"""
<VirtualHost *:80>
    ServerName {domain}
    ServerAlias www.{domain}
    DocumentRoot /home/{username}/{domain}/public_html
    
    ErrorLog /home/{username}/{domain}/logs/error.log
    CustomLog /home/{username}/{domain}/logs/access.log combined

    <Directory /home/{username}/{domain}/public_html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    <FilesMatch \.php$>
        SetHandler "proxy:unix:/var/run/php/php{php_version}-fpm.sock|fcgi://localhost"
    </FilesMatch>
</VirtualHost>
"""
        config_path = f"/etc/apache2/sites-available/{domain}.conf"
        
        if not LinuxService.is_linux():
            print(f"Mock: Creating VHost config for {domain}")
            return True

        try:
            with open(config_path, 'w') as f:
                f.write(vhost_config)
            
            subprocess.run(['a2ensite', domain], check=True)
            subprocess.run(['systemctl', 'reload', 'apache2'], check=True)
            return True
        except Exception as e:
            print(f"Error creating VHost: {e}")
            return False
