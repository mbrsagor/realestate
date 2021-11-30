from rest_framework import serializers
from inventory.models.inventory import Inventory
from inventory.serializers.category_serializer import TagSerializer


class InventorySerializer(serializers.ModelSerializer):
    tags = TagSerializer(source="name", read_only=True, many=True)

    class Meta:
        model = Inventory
        fields = [
            'id', 'name', 'category_name', 'tags', 'price', 'discount_price', 'stock_from', 'calculate_price',
            'variant', 'color', 'types', 'is_available', 'quantity', 'image', 'created_by', 'created_at', 'updated_at'
        ]
