from django.db import models
from utils import get_file_path
from django.urls import reverse
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
        return f'{self.name}-{self.family}'

    def get_absolute_url(self):
        return reverse('praiseres:detail', args=[self.id])

    def dirge_count(self):
        return self.related_dirges.count()

    def natals_count(self):
        return self.related_natals.count()
