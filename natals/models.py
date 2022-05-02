from django.db import models
from utils import get_file_path
from django_extensions.db.models import TimeStampedModel
from praiseres.models import Praiser


# Create your models here.
class NatalCategory(TimeStampedModel):
    title = models.CharField(
        max_length=255,
    )


class Natal(TimeStampedModel):
    category = models.ForeignKey(
        NatalCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='natals',
    )
    natal_name = models.CharField(
        max_length=255,
    )
    audio = models.FileField(
        upload_to=get_file_path
    )
    praiser = models.ForeignKey(
        Praiser,
        on_delete=models.CASCADE,
        related_name='natals',
    )

    def __str__(self):
        return f'{self.praiser} {self.natal_name}'
