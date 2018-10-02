"""Books models."""
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from postit.mixins import PreserveModelMixin


class Postit(PreserveModelMixin):
    """Base wrapper for a Postit type object."""

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=200,
        db_index=True,
    )
    user = models.OneToOneField(
        User,
        related_name='postits',
        verbose_name=_('User'),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Postit'
        verbose_name_plural = 'Postits'


class ListItem(PreserveModelMixin):
    """List Item model."""

    description = models.CharField(
        verbose_name=_('Description'),
        max_length=500,
        db_index=True,
    )
    completed_at = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        default=None,
    )
    postit = models.ForeignKey(
        Postit,
        related_name='list_items',
        verbose_name=_('Postit'),
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        verbose_name = 'Listed Item'
        verbose_name_plural = 'Listed Items'
