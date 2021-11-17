from django.contrib import admin


@admin.register
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'created_at',
                    'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
