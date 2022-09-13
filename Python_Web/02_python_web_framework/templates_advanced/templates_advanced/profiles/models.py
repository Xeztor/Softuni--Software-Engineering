from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        blank=True,
    )
    last_name = models.CharField(
        max_length=15,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )
    is_complete = models.BooleanField(
        default=False,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
