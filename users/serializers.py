from rest_framework.exceptions import ParseError, NotFound
from rest_framework import serializers
from clientes.models import Cliente
from .models import User, UserType


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Escolher entre " + " e".join(message) + "."


class UserSerializer(serializers.ModelSerializer):
    def update(self, instance: User, validated_data: dict):
        cliente = self.context["request"].data.get("cliente")
        senha = self.context["request"].data.get("senha")
        if cliente:
            if not senha:
                raise ParseError("É necessário informar uma senha para o usuário")

            cliente = Cliente.objects.filter(id=cliente).first()

            if not cliente:
                raise NotFound("Cliente não cadastrado")

            if not cliente.email:
                raise ParseError("É necessário o cliente ter um email cadastrado")

            instance.username = cliente.email
            instance.set_password(senha)

            instance.save()

            cliente.user = instance

            cliente.save()
        for key, value in validated_data.items():
            if not (key in ("user_type", "is_active")):
                raise ParseError(
                    "Só é permitido atualizar o tipo do usuário e/ou reativar usúario"
                )
            if key == "is_active":
                instance.date_disabled = None
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "user_type",
            "is_active",
            "date_disabled",
        ]
        extra_kwargs = {
            "user_type": {
                "error_messages": {
                    "invalid_choice": choices_error_message(UserType),
                }
            },
            "date_disabled": {"format": "%d-%m-%Y"},
        }
