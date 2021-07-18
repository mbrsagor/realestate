from django.db import models
from inventory.models.base import BaseEntity

from inventory.models.inventory import Inventory
from utils.enum import StockType


class Stock(BaseEntity):
    name = models.CharField(max_length=120)
    inventory_name = models.ForeignKey(Inventory, related_name='inventory_stock', on_delete=models.CASCADE)
    types = models.IntegerField(choices=StockType.select_type(), default=StockType.BUY.value)
    stock_out = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    buy_price = models.BooleanField(default=0)
    sell_price = models.BooleanField(default=0)

    def __str__(self):
        return self.name[:30]
