from django.db import models
from leads.models.base import BaseEntity


class Member(BaseEntity):
    alias = models.CharField(max_length=45)
    receiver_name = models.CharField(max_length=22)
    receiver_bank_account = models.CharField(max_length=17)
    receiver_phone_number = models.CharField(max_length=15, blank=True, null=True)
    receiver_email = models.CharField(max_length=100, blank=True, null=True)
    is_default_route = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    # objects = MemberManager()

    def __str__(self):
        return self.alias
