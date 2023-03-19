from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer
from .models import User


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


class UserDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance: User):
        instance.is_active = False
        instance.date_disabled = timezone.now()
        instance.save()
