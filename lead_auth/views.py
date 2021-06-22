from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.custom_responses import prepare_success_response, prepare_error_response
from .serializer import PositionSerializer, UserCategorySerializer
from .models import Position, UserCategory


class PositionAPIView(APIView):

    def get_object(self, pk):
        try:
            return Position.objects.filter(pk=pk).first()
        except Position.DoesNotExist:
            return None

    def get(self, request):
        try:
            instance = Position.objects.all()
            serializer = PositionSerializer(instance, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(prepare_error_response(str(e)), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        pass
