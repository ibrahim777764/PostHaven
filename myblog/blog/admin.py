from django.contrib import admin
from .models import Post


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')

admin.site.register(Post, AdminPost)
