"""Books admin."""

from django.contrib import admin

from postit.models import Postit, ListItem


@admin.register(Postit)
class PostitAdmin(admin.ModelAdmin):
    """Postit admin."""

    list_display = (
        'id',
        'title',
    )
    search_fields = (
        'title__icontains',
        'list_items__description__icontains',
    )
    list_filter = ('title',)
    exclude = (
        'created_at',
        'modified_at',
        'deleted_at',
    )


@admin.register(ListItem)
class BookProgressAdmin(admin.ModelAdmin):
    """BookProgress admin."""

    list_display = (
        'id',
        'description',
        'postit',
    )
    search_fields = (
        'postit__title',
        'description',
    )
    list_filter = ('description',)
    exclude = (
        'created_at',
        'modified_at',
        'deleted_at',
    )
