from django.contrib import admin

from inventory.models.category import Category, Tag
from inventory.models.inventory import Inventory

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Inventory)
