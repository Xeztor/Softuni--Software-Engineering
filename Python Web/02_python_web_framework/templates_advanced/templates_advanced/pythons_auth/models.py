from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class PythonsUserManager(UserManager):
    pass


class PythonsUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20,
        unique=True,
    )
    email = models.EmailField()

    USERNAME_FIELD = 'username'

    is_staff = models.BooleanField(
        default=False,
    )

    objects = UserManager()
