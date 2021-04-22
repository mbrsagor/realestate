from leads.models.member import Member
from leads.serializers.member_serializer import MemberSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MemberListAPIView(APIView):
    def get(self, request):
        pass
