from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.category_validation import validation_category_data
from utils.custom_responses import prepare_error_response, prepare_create_success_response, prepare_success_response
from inventory.models.category import Category
from inventory.serializers.category_serializer import CategorySerializer


class CategoryAPIView(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.filter(id=pk).first()
        except Category.DoesNotExist:
            return None

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        validation_error = validation_category_data(request.data)
        if validation_error is not None:
            return Response(prepare_error_response(validation_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            category.delete()
            return Response(prepare_success_response("Category deleted successfully"), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)
