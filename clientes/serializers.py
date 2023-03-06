from rest_framework import serializers
from users.serializers import UserSerializer
from users.models import User
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            "id",
            "nomeCliente",
            "sexo",
            "pessoa_fisica",
            "documento",
            "telefone",
            "celular",
            "email",
            "dataCadastro",
            "rua",
            "numero",
            "bairro",
            "cidade",
            "estado",
            "cep",
            "contato",
            "complemento",
            "fornecedor",
        ]


class ClienteWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def update(self, instance: Cliente, validated_data: dict):
        user_data = validated_data.pop("user")

        user = User.objects.create_user(**user_data)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.user = user

        instance.user.nome = instance.nomeCliente

        instance.save()

        return instance

    class Meta:
        model = Cliente
        fields = [
            "id",
            "nomeCliente",
            "sexo",
            "pessoa_fisica",
            "documento",
            "telefone",
            "celular",
            "email",
            "dataCadastro",
            "rua",
            "numero",
            "bairro",
            "cidade",
            "estado",
            "cep",
            "contato",
            "complemento",
            "fornecedor",
            "user",
        ]
        read_only_fields = [
            "nomeCliente",
            "sexo",
            "pessoa_fisica",
            "documento",
            "telefone",
            "celular",
            "email",
            "dataCadastro",
            "rua",
            "numero",
            "bairro",
            "cidade",
            "estado",
            "cep",
            "contato",
            "complemento",
            "fornecedor",
        ]
