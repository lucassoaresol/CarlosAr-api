from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
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
            "username",
            "senha",
            "user_type",
        ]
        extra_kwargs = {"senha": {"write_only": True, "source": "password"}}
