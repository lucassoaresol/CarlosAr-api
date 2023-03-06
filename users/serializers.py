from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "senha":
                instance.set_password(value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "nome",
            "rg",
            "cpf",
            "cep",
            "rua",
            "numero",
            "bairro",
            "cidade",
            "estado",
            "username",
            "email",
            "senha",
            "telefone",
            "celular",
            "is_active",
            "dataCadastro",
            "dataExpiracao",
            "url_image_user",
        ]
        extra_kwargs = {"senha": {"write_only": True, "source": "password"}}
