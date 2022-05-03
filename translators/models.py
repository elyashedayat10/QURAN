import os

from django.db import models
from django.utils.encoding import smart_str
from django_extensions.db.models import TimeStampedModel
from utils import get_file_path


def get_audio_path(instance, filename):
    qari = smart_str(instance.qari.last_name)
    directory = 'audio/' + '/' + qari
    if not os.path.exists(directory):
        os.makedirs(directory)
    full_path = str(directory) + "/%s" % (filename)
    return full_path


class Ayeh(models.Model):
    pass


class Translator(TimeStampedModel):
    first_name = models.CharField(max_length=125, verbose_name="نام")
    last_name = models.CharField(max_length=125, verbose_name="نام خانوادگی")
    image = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

    class Meta:
        verbose_name = "مترجم"
        verbose_name_plural = "مترجمان"


class QuranTranslateAudio(TimeStampedModel):
    ayeh = models.ForeignKey(Ayeh, on_delete=models.CASCADE, verbose_name="آیه", related_name="translate_qari")
    qari = models.ForeignKey(Translator, on_delete=models.CASCADE, verbose_name="قاری")
    audio = models.FileField(upload_to=get_audio_path, verbose_name="صوت")
    text = models.TextField()

    class Meta:
        verbose_name = "صوت قرآن"
        verbose_name_plural = "صوت های قرآن"
