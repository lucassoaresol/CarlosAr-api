from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.permissions import IsAuthFunc
from users.models import User
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
