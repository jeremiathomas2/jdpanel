from django.urls import path
from . import views

app_name = 'ssl'

urlpatterns = [
    path('', views.certificate_list, name='list'),
    path('auto-install/', views.auto_install, name='auto_install'),
    path('custom-upload/', views.custom_upload, name='custom_upload'),
]
