from django.db import models


class StatusType(models.TextChoices):
    DRAFT = ("DRAFT", "پیش‌نویس")
    PUBLISHED = ("PUBLISHED", "منتشر شده")
    PENDING = ("PENDING", "در حال بررسی")
    BACK = ("BACK", "برگشت داده شده")
