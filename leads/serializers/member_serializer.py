from leads.models.member import Member
from rest_framework import serializer


class MemberSerializer(serializer.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
