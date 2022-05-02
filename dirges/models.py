from django.db import models
from utils import TimestampModel, get_file_path


# Create your models here.
class DirgeCategory(TimestampModel):
    title = models.CharField(max_length=255)


class Dirge(TimestampModel):
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
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name='dirges',
    )

    def __str__(self):
        return f'{self.singer} {self.dirge_name}'
