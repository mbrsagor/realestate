from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import PositionSerializer, UserCategorySerializer
from .models import Position, UserCategory


class PositionAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass
