from django.db import models


class LeadQuerySetManager(models.Manager):
    def get_users_leads(self, username):
        return self.filter(author__username=username)


class LeadManager(models.Manager):
    def get_queryset(self):
        return LeadQuerySetManager(self.model, using=self._db)

    def get_users_leads(self, username):
        return self.get_queryset().get_users_leads(username)
