from django.urls import path
from .views import ClienteView, ClienteDetailView

urlpatterns = [
    path("clientes/", ClienteView.as_view()),
    path("clientes/<uuid:pk>/", ClienteDetailView.as_view()),
]
