from django.db import models
from leads.models.base import BaseEntity


class SagorBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Mbr Sagor')


class Book(BaseEntity):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)


    objects = models.Manager() # The default manager.
    sagor_objects = SagorBookManager() # The Sagor-specific manager.

    def __str__(self):
        return self.title
