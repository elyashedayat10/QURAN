from django.db import models
from django.urls import reverse

from utils import get_file_path
from django_extensions.db.models import TimeStampedModel
from praiseres.models import Praiser


# Create your models here.
class NatalCategory(TimeStampedModel):
    title = models.CharField(
        max_length=255,
    )
    logo = models.ImageField(upload_to=get_file_path, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('natals:category_detail', args=[self.id])

    def natals_count(self):
        return self.natals.count()

    def praiser_count(self):
        return Praiser.objects.filter(related_dirges__category__title__exact=self.title).count()


class Natal(TimeStampedModel):
    category = models.ForeignKey(
        NatalCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='natals',
    )
    name = models.CharField(
        max_length=255,
    )
    audio = models.FileField(
        upload_to=get_file_path
    )
    praiser = models.ForeignKey(
        Praiser,
        on_delete=models.CASCADE,
        related_name='related_natals',
    )

    def __str__(self):
        return f'{self.praiser} {self.name}'
