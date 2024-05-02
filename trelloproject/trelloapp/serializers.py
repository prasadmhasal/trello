from rest_framework import serializers
from .models import Column, Card

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','password']

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['title', 'position']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['title', 'description', 'position', 'column']