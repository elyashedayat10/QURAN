from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ("مرد", "مرد"),
        ("زن", "زن"),
    )
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    REQUIRED_FIELDS = ["full_name", "email"]
    USERNAME_FIELD = "phone_number"

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"
