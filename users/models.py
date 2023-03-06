from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nome = models.CharField(max_length=255)
    dataCadastro = models.DateField(auto_now_add=True)
    dataExpiracao = models.DateField(null=True)
    url_image_user = models.CharField(
        max_length=255,
        null=True,
    )
