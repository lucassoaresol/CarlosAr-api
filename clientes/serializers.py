from rest_framework import serializers
from rest_framework.exceptions import ParseError
from enderecos.serializers import EnderecoSerializer
from enderecos.models import Endereco
from users.serializers import UserSerializer
from users.models import User
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    user = UserSerializer(read_only=True)
    senha = serializers.CharField(
        max_length=128,
        write_only=True,
        required=False,
    )

    def create(self, validated_data: dict):
        endereco_data = validated_data.pop("endereco")
        try:
            email = validated_data.get("email")
            senha = validated_data.pop("senha")

            user_type = "Cliente"
            funcionario = validated_data.get("funcionario")

            if funcionario:
                user_type = "Funcionário"

            if not email:
                raise ParseError("É necessário informar um email para criar um usuário")

            user_data = {
                "username": email,
                "password": senha,
                "user_type": user_type,
            }

            user = User.objects.create_user(**user_data)

            cliente = Cliente.objects.create(**validated_data, user=user)
            Endereco.objects.create(**endereco_data, cliente=cliente)

            return cliente
        except KeyError:
            cliente = Cliente.objects.create(**validated_data)
            Endereco.objects.create(**endereco_data, cliente=cliente)

            return cliente

    def update(self, instance: Cliente, validated_data: dict):
        try:
            email = validated_data.get("email")
            senha = validated_data.pop("senha")

            user_type = "Cliente"
            funcionario = validated_data.get("funcionario")

            if funcionario:
                user_type = "Funcionário"

            if not email:
                email = instance.email
                if not email:
                    raise ParseError(
                        "É necessário informar um email para criar um usuário"
                    )

            for key, value in validated_data.items():
                setattr(instance, key, value)

            user = instance.user

            user_data = {
                "username": email,
                "password": senha,
                "user_type": user_type,
            }

            if not user:
                user = User.objects.create_user(**user_data)
                instance.user = user

                instance.save()

                return instance

            for key, value in user_data.items():
                setattr(user, key, value)

                if key == "password":
                    user.set_password(value)

            user.save()
            instance.save()

            return instance
        except KeyError:
            for key, value in validated_data.items():
                setattr(instance, key, value)

            user = instance.user

            if user:
                email = validated_data.get("email")
                if email:
                    user.email = email
                    user.save()

                funcionario = validated_data.get("funcionario")
                if funcionario:
                    user.user_type = "Funcionário"
                    user.save()

            instance.save()

            return instance

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
            "endereco",
            "user",
            "senha",
        ]
