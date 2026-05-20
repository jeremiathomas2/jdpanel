from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('websites/', views.websites, name='websites'),
    path('databases/', views.databases, name='databases'),
    path('emails/', views.emails, name='emails'),
]
