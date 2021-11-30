from rest_framework import serializers

from inventory.models import Tag
from inventory.models.inventory import Inventory


class TagSerializer(serializers.ModelSerializer):
    # name = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Tag
        fields = (
            'id', 'name'
        )


class InventorySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        # depth = 1
        model = Inventory
        fields = [
            'id', 'name', 'category_name', 'tags', 'price', 'discount_price', 'stock_from', 'calculate_price',
            'variant', 'color', 'types', 'is_available', 'quantity', 'image', 'created_by', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        inventory = Inventory.objects.create(**validated_data)
        for tag in tags:
            inventory.tags.add(tag.save())
        return inventory
