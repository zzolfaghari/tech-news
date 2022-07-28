from django.db import models

from django.utils import timezone

from base.enums import StatusType
from shared.utils import TechNewsUtils


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status=StatusType.PUBLISHED)


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, default=None, blank=True, null=True, verbose_name="زیر دسته")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField()

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articles")
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=StatusType.choices)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def jpublish(self):
        return TechNewsUtils().jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    objects = ArticleManager()
