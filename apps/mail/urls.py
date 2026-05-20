from django.urls import path
from . import views

app_name = 'mail'

urlpatterns = [
    path('', views.mail_list, name='list'),
    path('create/', views.account_create, name='create'),
    path('auto-responders/', views.auto_responders, name='auto_responders'),
    path('spam-filters/', views.spam_filters, name='spam_filters'),
    path('dkim-spf/', views.dkim_spf, name='dkim_spf'),
]
