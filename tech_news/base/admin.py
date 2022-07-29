from django.contrib import admin

from base.enums import StatusType
from base.models import Article, Category


def make_published(modeladmin, request, queryset):
    queryset.update(status=StatusType.PUBLISHED)


make_published.short_description = "انتشار مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = dict(slug=('title',))


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'show_category')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = dict(slug=('title',))
    ordering = ['status', 'publish']
    actions = [make_published]

    def show_category(self, obj):
        return "، ".join([category.title for category in obj.category_published()])

    show_category.short_description = "دسته‌بندی"


admin.site.register(Article, ArticleAdmin)
