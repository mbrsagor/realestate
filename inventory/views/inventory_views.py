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


class InventoryUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Inventory.objects.filter(id=pk).first()
        except Inventory.DoesNotExist:
            return None

    def put(self, request, pk, format=None):
        validation_error = validation_inventory_data(request.data)
        if validation_error is not None:
            return Response(prepare_error_response(validation_error), status=status.HTTP_400_BAD_REQUEST)
        inventory = Inventory.objects.filter(id=pk).first()
        if inventory is not None:
            serializer = InventorySerializer(inventory, data=request.data)
            if serializer.is_valid():
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(prepare_error_response("No Inventory found for this ID"),
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inventory = self.get_object(pk)
        if inventory is not None:
            inventory.delete()
            return Response(prepare_success_response("Inventory deleted successfully"), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)
