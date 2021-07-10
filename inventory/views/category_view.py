from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inventory.models.category import Category
from inventory.serializers.category_serializer import CategorySerializer


class CategoryAPIView(APIView):

    def get_object(self, pk):
        pass

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk):
        pass
