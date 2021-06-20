from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.db import models


class CustomUserManager(BaseUserManager):
    """
        Custom user model manager where email is the unique identifiers
        for authentication instead of usernames.
        """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Position(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class UserCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True, blank=True)
    category_role = models.ManyToManyField(Group, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class LeadUser(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=11, unique=True)
    fullname = models.CharField(max_length=100, blank=True)
    designation = models.ForeignKey(Position, null=True, blank=True, on_delete=models.CASCADE)
    user_category = models.ForeignKey(UserCategory, null=True, blank=True, on_delete=models.CASCADE)
    user_note = models.TextField(verbose_name='user Note', blank=True, )
    is_supportUser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)


class VerifiedPhone(models.Model):
    phone_number = models.CharField(max_length=14)
    otp_code = models.CharField(max_length=6)
    tracking_id = models.CharField(max_length=50)
    otp_verify = models.BooleanField(default=False)
    expire_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    next_available_try = models.IntegerField(default=3, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['phone_number', 'tracking_id']),
        ]

    def __str__(self):
        return f"{self.pk, self.phone_number}"
