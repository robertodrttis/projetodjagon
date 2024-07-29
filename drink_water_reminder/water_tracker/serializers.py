from rest_framework import serializers
from .models import User, WaterIntake

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'weight']

class WaterIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterIntake
        fields = ['id', 'user', 'date', 'amount']
