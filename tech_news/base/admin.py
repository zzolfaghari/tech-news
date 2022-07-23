from django.contrib import admin

from base.models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title', 'slug', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = dict(slug=('title',))


admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = dict(slug=('title',))
    ordering = ['status', 'publish']


admin.site.register(Article, ArticleAdmin)
