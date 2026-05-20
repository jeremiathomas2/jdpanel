from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.websites.models import Website
from apps.databases.models import Database
from apps.mail.models import EmailAccount
from .serializers import WebsiteSerializer, DatabaseSerializer, EmailSerializer

class WebsiteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteSerializer
    
    def get_queryset(self):
        return Website.objects.filter(user=self.request.user)

class DatabaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DatabaseSerializer
    
    def get_queryset(self):
        return Database.objects.filter(user=self.request.user)

class EmailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmailSerializer
    
    def get_queryset(self):
        return EmailAccount.objects.filter(user=self.request.user)
