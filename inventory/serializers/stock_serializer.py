from rest_framework import serializers
from inventory.models.stock import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'id', 'name', 'inventory_name', 'types', 'stock_out', 'quantity', 'buy_price', 'sell_price',
            'created_by', 'created_at', 'updated_at'
        ]
