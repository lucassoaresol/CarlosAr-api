from rest_framework import permissions
from rest_framework.views import View, Request
from .models import User


class IsAdminUserList(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method == "POST":
            return True

        return req.user.is_superuser


class IsAuthFunc(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        return (
            req.user.is_superuser
            or req.user.is_authenticated
            and req.user.user_type == "Funcionário"
        )


class IsAuthEmployee(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: User):
        return req.user.is_superuser or req.user.is_authenticated and obj == req.user
