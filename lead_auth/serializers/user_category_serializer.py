from rest_framework import serializers

from lead_auth.models import UserCategory


class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = '__all__'
