from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from lead_auth.serializers.user_category_serializer import UserCategorySerializer
from utils.custom_responses import prepare_success_response, prepare_error_response, prepare_create_success_response
from lead_auth.services.validation_service import validate_position_data
from lead_auth.models import UserCategory


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

    def post(self, request):
        validate_error = validate_position_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = UserCategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        validate_error = validate_position_data(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        user_category = UserCategory.objects.filter(id=pk).first()
        if user_category is not None:
            serializer = UserCategorySerializer(user_category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(prepare_error_response('No data found for this ID'), status=status.HTTP_400_BAD_REQUEST)
