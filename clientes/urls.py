from django.urls import path
from .views import ClienteView, ClienteDetailView, ClienteWithUserView

urlpatterns = [
    path("clientes/", ClienteView.as_view()),
    path("clientes/<int:pk>/", ClienteDetailView.as_view()),
    path("clientes/<int:pk>/user/", ClienteWithUserView.as_view()),
]
