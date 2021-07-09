from django.db import models
from inventory.models.base import BaseEntity


class Category(BaseEntity):
    name = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='category', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parent_category')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name[:30]


class Tag(BaseEntity):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name[:30]
