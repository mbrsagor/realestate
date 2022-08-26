import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManger


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.URLField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=150, verbose_name=_('First name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Last name'))
    username = models.CharField(max_length=100, verbose_name=_('Username'), unique=True)
    email = models.EmailField(verbose_name=_('Email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self): return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def short_name(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    object = CustomUserManger()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
