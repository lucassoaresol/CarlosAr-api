from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .models import Cliente
from .serializers import ClienteSerializer, ClienteWithUserSerializer


class ClienteView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ClienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ClienteWithUserView(UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteWithUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
