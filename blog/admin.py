from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('uid', 'user', 'type')
    readonly_fields = ('uid', 'created', 'updated',)
    search_fields = ('user', 'uid')
    list_filter = ('type',)
    list_select_related = ('user',)
    autocomplete_fields = ('user',)


admin.site.register(Post, PostAdmin)
