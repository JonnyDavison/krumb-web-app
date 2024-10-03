from rest_framework import serializers
from .models import UserProfile, WholesaleProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'is_wholesale']

class WholesaleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholesaleProfile
        fields = ['id', 'user_profile', 'company_name', 'tax_id', 'approved']