from rest_framework import serializers
from inventory.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'parent', 'is_active', 'category_image',
            'created_by', 'created_at', 'updated_at'
        ]
