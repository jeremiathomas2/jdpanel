from django.urls import path
from . import views

app_name = 'backups'

urlpatterns = [
    path('', views.backup_manager, name='manager'),
    path('schedules/', views.backup_schedules, name='schedules'),
    path('restore/', views.backup_restore, name='restore'),
    path('remote-storage/', views.remote_storage, name='remote_storage'),
]
