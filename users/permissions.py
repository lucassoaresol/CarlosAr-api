from rest_framework import permissions
from rest_framework.views import View, Request


class IsAdminUserList(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method == "POST":
            return True

        return req.user.is_superuser
