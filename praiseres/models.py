from django.db import models
from utils import get_file_path
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Praiser(TimeStampedModel):
    name = models.CharField(
        max_length=255,
    )
    family = models.CharField(
        max_length=255,
    )
    image = models.ImageField(
        upload_to=get_file_path,
    )

    def __str__(self):
        return self.name
