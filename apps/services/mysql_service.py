import subprocess
import platform

class MySQLService:
    @staticmethod
    def is_linux():
        return platform.system() == "Linux"

    @staticmethod
    def create_database(db_name):
        if not MySQLService.is_linux():
            print(f"Mock: Creating database {db_name}")
            return True
        
        try:
            # Using mysql command line (requires root or a user with CREATE permissions)
            cmd = f"CREATE DATABASE {db_name};"
            subprocess.run(['mysql', '-e', cmd], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def create_user(username, password, db_name):
        if not MySQLService.is_linux():
            print(f"Mock: Creating DB user {username} for {db_name}")
            return True

        try:
            cmd = f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'; GRANT ALL PRIVILEGES ON {db_name}.* TO '{username}'@'localhost'; FLUSH PRIVILEGES;"
            subprocess.run(['mysql', '-e', cmd], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
