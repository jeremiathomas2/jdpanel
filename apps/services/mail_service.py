import subprocess
import platform

class MailService:
    @staticmethod
    def is_linux():
        return platform.system() == "Linux"

    @staticmethod
    def create_email_account(email, password, quota_mb):
        if not MailService.is_linux():
            print(f"Mock: Creating email {email} with password and quota {quota_mb}MB")
            return True

        # Real logic would involve:
        # 1. Updating virtual mailbox table (usually in MySQL if using Postfix/Dovecot with DB)
        # 2. Creating directory /var/vmail/domain/user
        # 3. Reloading postfix/dovecot
        return True

    @staticmethod
    def create_forwarder(source, destination):
        if not MailService.is_linux():
            print(f"Mock: Forwarding {source} to {destination}")
            return True
        return True
