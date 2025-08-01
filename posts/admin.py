from django.contrib import admin

from .models import Post, Comment


class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'publish_date', 'created_time', 'updated_time']
    inlines = [CommentAdminInline]


admin.site.register(Comment)