from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManger(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(_('you must provide a valid email address'))

    def create_user(self, username, email, first_name, last_name, password, **extra_fields):
        if not username:
            raise ValueError(_('you must provide a username.'))
        if not first_name:
            raise ValueError(_('you must provide a first name.'))
        if not last_name:
            raise ValueError(_('you must provide a last name.'))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('you must provide an email.'))

        user = self.model(
            username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))

        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must have is_active=True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        if not password:
            raise ValueError(_("Superuser must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('you must provide an email.'))

        user = self.model(
            username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
