from django.db import models

from django.utils import timezone

from base.enums import StatusType


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=StatusType.choices)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
