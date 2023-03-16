from rest_framework import serializers
from users.serializers import UserSerializer
from users.models import User
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    def create(self, validated_data: dict):
        email = validated_data.get("email")
        senha = self.context["request"].data.get("senha")

        if email and senha:
            user = User.objects.create_user(
                username=email,
                password=senha,
            )

        return Cliente.objects.create(**validated_data, user=user)

    class Meta:
        model = Cliente
        fields = [
            "id",
            "nome",
            "documento",
            "email",
            "celular",
            "telefone",
            "pessoa_fisica",
            "funcionario",
            "fornecedor",
            "data_cadastro",
            "user",
        ]
