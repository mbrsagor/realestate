from django.db import models
from lead_auth.models import LeadUser


class BaseEntity(models.Model):
    created_by = models.ForeignKey(LeadUser, on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
