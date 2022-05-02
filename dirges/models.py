from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.urls import reverse
from praiseres.models import Praiser
from utils import get_file_path


# Create your models here.
class DirgeCategory(TimeStampedModel):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=get_file_path, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dirges:category_detail', args=[self.id])

    def dirges_count(self):
        return self.dirges.count()

    def praiser_count(self):
        return Praiser.objects.filter(related_dirges__category__title__exact=self.title).count()


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
        related_name='related_dirges',
    )
    logo = models.ImageField(upload_to=get_file_path, blank=True)

    def __str__(self):
        return f'{self.praiser} {self.dirge_name}'
