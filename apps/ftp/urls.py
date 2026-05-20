from django.urls import path
from . import views

app_name = 'ftp'

urlpatterns = [
    path('', views.account_list, name='list'),
    path('logs/', views.ftp_logs, name='logs'),
]
