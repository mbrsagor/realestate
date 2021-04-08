from django.db import models
from leads.models.base import BaseEntity


class Lead(BaseEntity):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=80, unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
