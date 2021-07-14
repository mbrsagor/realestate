from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inventory.models.inventory import Inventory
from inventory.serializers.inventory_serializer import InventorySerializer
from utils.inventory_validation import validation_inventory_data
from utils.custom_responses import prepare_error_response, prepare_create_success_response, prepare_success_response


class InventoryAPIView(APIView):
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        validation_error = validation_inventory_data(request.data)
        if validation_error is not None:
            return Response(prepare_error_response(validation_error), status=status.HTTP_400_BAD_REQUEST)

        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
