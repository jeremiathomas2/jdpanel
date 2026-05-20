from rest_framework import serializers
from apps.websites.models import Website
from apps.databases.models import Database
from apps.mail.models import EmailAccount

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'

class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAccount
        fields = '__all__'
