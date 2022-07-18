from django.db import models


class StatusType(models.TextChoices):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
