from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from lead_auth.serializers.user_category_serializer import UserCategorySerializer
from lead_auth.models import UserCategory
from utils.custom_responses import prepare_success_response, prepare_error_response


class UserCategoryAPIView(APIView):
    def get_object(self, pk):
        try:
            return UserCategory.objects.filter(id=pk).first()
        except UserCategory.DoesNotExist:
            return None

    def get(self, request):
        try:
            user_category = UserCategory.objects.all()
            serializer = UserCategorySerializer(user_category, data=request.data)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(prepare_error_response(str(e)), status=status.HTTP_400_BAD_REQUEST)
