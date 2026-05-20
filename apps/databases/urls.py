from django.urls import path
from . import views

app_name = 'databases'

urlpatterns = [
    path('', views.database_list, name='list'),
    path('create/', views.database_create, name='create'),
    path('user/create/', views.database_user_create, name='user_create'),
]
