from django.db import models
from django_extensions.db.models import TimeStampedModel

from praiseres.models import Praiser
from utils import get_file_path


# Create your models here.
class DirgeCategory(TimeStampedModel):
    title = models.CharField(max_length=255)


class Dirge(TimeStampedModel):
    category = models.ForeignKey(
        DirgeCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='dirges',
    )
    dirge_name = models.CharField(
        max_length=255,
    )
    audio = models.FileField(
        upload_to=get_file_path
    )
    praiser = models.ForeignKey(
        Praiser,
        on_delete=models.CASCADE,
        related_name='dirges',
    )

    def __str__(self):
        return f'{self.praiser} {self.dirge_name}'
