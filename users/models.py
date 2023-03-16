from django.contrib.auth.models import AbstractUser
from django.db import models


class UserType(models.TextChoices):
    ADMINISTRADOR = "Administrador"
    FUNCIONARIO = "Funcionário"
    CLIENTE = "Cliente"


class User(AbstractUser):
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.CLIENTE,
    )
