from django.contrib import admin

from apps.blog.models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'intro', 'created_at',
                    'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'intro', 'created_at')
    list_filter = ('category', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'email', 'body', 'created_at')
    search_fields = ('name', 'post', 'email', 'body', 'created_at')
    list_filter = ('name', 'post', 'created_at')

