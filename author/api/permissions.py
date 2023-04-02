from rest_framework import permissions

from reader.models import UserRoles


class IsAdmin(permissions.BasePermission):
    message = 'Вы не являетесь админом.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRoles.ADMIN:
            return True
        return False


class IsOwner(permissions.BasePermission):
    message = 'Редактировать и удалять может только владелец.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRoles.OWNER:
            return True
        return False

