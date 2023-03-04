from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nome = models.CharField(max_length=80)
    rg = models.CharField(
        max_length=20,
        null=True,
    )
    cpf = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    rua = models.CharField(
        max_length=70,
        null=True,
    )
    numero = models.CharField(
        max_length=15,
        null=True,
    )
    bairro = models.CharField(
        max_length=45,
        null=True,
    )
    cidade = models.CharField(
        max_length=45,
        null=True,
    )
    estado = models.CharField(
        max_length=20,
        null=True,
    )
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(
        max_length=20,
        null=True,
    )
    dataCadastro = models.DateField(auto_now_add=True)
    dataExpiracao = models.DateField(null=True)
    url_image_user = models.CharField(
        max_length=255,
        null=True,
    )
