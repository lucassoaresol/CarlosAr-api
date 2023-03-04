from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
