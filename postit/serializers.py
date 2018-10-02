"""Books app serializers."""

from rest_framework import serializers

from postit.models import Postit, ListItem


class PostitSerializer(serializers.HyperlinkedModelSerializer):
    """Postit serializer."""

    id = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='postit-detail',
    )

    class Meta:
        model = Postit
        read_only_fields = (
            'id',
        )
        fields = read_only_fields + (
            'title',
            'list_items',
        )
        exclude = []


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    """Postit List Item serializer."""

    id = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='listitem-detail',
    )

    class Meta:
        model = ListItem
        read_only_fields = (
            'id',
        )
        fields = read_only_fields + (
            'description',
            'completed_at',
            'postit',
        )
        exclude = []
