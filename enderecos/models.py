import uuid
from django.db import models


class Endereco(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
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
    cep = models.CharField(
        max_length=20,
        null=True,
    )
    complemento = models.CharField(
        max_length=45,
        null=True,
    )

    cliente = models.OneToOneField(
        "clientes.cliente",
        on_delete=models.CASCADE,
        related_name="endereco",
    )
