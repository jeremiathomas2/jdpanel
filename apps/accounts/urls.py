from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-change/', views.password_change, name='password_change'),
    path('2fa/', views.security_2fa, name='security_2fa'),
]
