from django.urls import path
from . import views

app_name = 'dns'

urlpatterns = [
    path('', views.zone_list, name='zone_list'),
    path('records/<int:zone_id>/', views.record_list, name='record_list'),
    path('propagation/', views.propagation_check, name='propagation_check'),
]
