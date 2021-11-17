from django.contrib import admin

from apps.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'created_at',
                    'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
