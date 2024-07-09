from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    """
    Custom permission to only allow doctors to create, update, or delete.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the 'doctor' role
        return request.user.is_authenticated and request.user.role == 'doctor'
