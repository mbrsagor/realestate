from django.contrib.auth.models import User
from django.db import models
from leads.models.base import BaseEntity


class Lead(BaseEntity):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=80, unique=True)
    message = models.TextField()
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.name
