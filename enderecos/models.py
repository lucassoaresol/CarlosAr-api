from django.db import models


class Endereco(models.Model):
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

    user = models.OneToOneField(
        "users.user",
        on_delete=models.CASCADE,
        related_name="endereco",
    )
