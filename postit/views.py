"""Books app views."""

import logging

from rest_framework import (viewsets, filters)

from postit.models import Postit, ListItem
from postit.permissions import OwnerPermission
from postit.serializers import PostitSerializer, ListItemSerializer

logger = logging.getLogger(__name__)


class PostitViewSet(viewsets.ModelViewSet):
    queryset = Postit.objects.all()
    serializer_class = PostitSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'title',
        'list_items__description',
    )
    permission_classes = (OwnerPermission, )


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'description',
        'completed_at',
        'postit__title',
    )
    permission_classes = (OwnerPermission, )
