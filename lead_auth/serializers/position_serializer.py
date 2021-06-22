from rest_framework import serializers

from lead_auth.models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
