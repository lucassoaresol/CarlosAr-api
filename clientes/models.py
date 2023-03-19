import uuid
from django.db import models


class Cliente(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=20)
    email = models.EmailField(
        max_length=100,
        unique=True,
        null=True,
    )
    celular = models.CharField(max_length=20)
    telefone = models.CharField(
        max_length=20,
        null=True,
    )
    pessoa_fisica = models.BooleanField(default=True)
    funcionario = models.BooleanField(default=False)
    fornecedor = models.BooleanField(default=False)
    data_cadastro = models.DateField(auto_now_add=True)

    user = models.OneToOneField(
        "users.user",
        on_delete=models.CASCADE,
        related_name="cliente",
        null=True,
    )
