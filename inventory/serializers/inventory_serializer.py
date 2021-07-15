from rest_framework import serializers
from inventory.models.inventory import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id', 'name', 'category_name', 'tags', 'price', 'discount_price', 'stock_from', 'calculate_price',
            'color', 'types', 'is_available', 'quantity', 'image', 'created_by', 'created_at', 'updated_at'
        ]
