from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('websites/', views.websites_list, name='websites'),
    path('databases/', views.databases_list, name='databases'),
    path('emails/', views.emails_list, name='emails'),
]
