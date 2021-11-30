from django.db import models
from django.db.models import JSONField
from inventory.models.base import BaseEntity
from inventory.models.category import Category
from inventory.models.category import Tag

from utils.enum import InventoryTypes


class Inventory(BaseEntity):
    name = models.CharField(max_length=120)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='inventory_category')
    tags = models.ManyToManyField(Tag, related_name='inventory_tag', blank=True)
    color = models.CharField(max_length=30)
    variant = JSONField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=12, default=0.00, decimal_places=12)
    discount_price = models.DecimalField(max_digits=12, default=0.00, decimal_places=12)
    stock_from = models.CharField(max_length=120)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='inventory', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    types = models.IntegerField(choices=InventoryTypes.get_choices(), default=InventoryTypes.KG.value)

    def __str__(self):
        return f"{self.id} {self.name}"

    def calculate_price(self):
        price = int(self.price)
        return self.quantity * price
