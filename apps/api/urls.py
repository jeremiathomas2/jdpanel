from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'websites', views.WebsiteViewSet, basename='website')
router.register(r'databases', views.DatabaseViewSet, basename='database')
router.register(r'emails', views.EmailViewSet, basename='email')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
