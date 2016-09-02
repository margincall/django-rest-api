from django.contrib import admin

from .models import User
from apps.artist.models import Artist


class ArtistInline(admin.TabularInline):
    model = Artist

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        ArtistInline,
    ]
