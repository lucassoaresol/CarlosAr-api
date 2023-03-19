from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.permissions import IsAuthFunc
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthFunc]


class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthFunc]

    def perform_destroy(self, instance: Cliente):
        user = instance.user
        if user:
            user.is_active = False
            user.date_disabled = timezone.now()
            user.save()
        return super().perform_destroy(instance)
