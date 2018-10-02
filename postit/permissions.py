"""Books policies."""

import logging

from rest_framework import permissions

logger = logging.getLogger(__name__)


class OwnerPermission(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        """Owner and admin have access."""
        authenticated = super().has_permission(request, view)
        return (
            authenticated and
            (
                (
                        hasattr(obj, 'user') and
                        obj.user.id == request.user.id
                ) or
                (
                        hasattr(obj, 'postit') and
                        obj.postit.user == request.user.id
                )
            )
        )
