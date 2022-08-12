from rest_framework import permissions


class UpdateOwnContact(permissions.BasePermission):
    """Allow user to update their own contacts."""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own contacts."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
