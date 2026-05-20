from django.urls import path
from . import views

app_name = 'websites'

urlpatterns = [
    path('', views.website_list, name='list'),
    path('create/', views.website_create, name='create'),
    path('delete/<int:pk>/', views.website_delete, name='delete'),
    path('file-manager/', views.file_manager, name='file_manager'),
]
