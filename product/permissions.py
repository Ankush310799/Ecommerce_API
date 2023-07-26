
from rest_framework import permissions


class ForProductHandlingPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_owner:
            return True

        return False


class ForProductList(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.is_owner:
            return True

        if request.user.is_authenticated:
            return True

        if request.user.is_annonymous:
            return True

        return False
