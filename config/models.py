from django.db import models
from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel
from utils import (
    get_file_path,
    validate_only_one_instance,
)


# Create your models here.
class BaseConfig(models.Model):
    title = models.CharField(
        max_length=125,
    )
    image = models.ImageField(
        upload_to=get_file_path,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class SiteSetting(TimeStampedModel, BaseConfig):

    def clean(self):
        validate_only_one_instance(self)


class Slider(TimeStampedModel, BaseConfig):
    is_active = models.BooleanField(
        default=True,
    )


class AboutUs(TimeStampedModel):
    title = models.CharField(
        max_length=125,
    )
    description = RichTextField()

    def __str__(self):
        return self.title

    def clean(self):
        validate_only_one_instance(self)


class ContactUS(TimeStampedModel):
    full_name = models.CharField(
        max_length=255,
    )
    title = models.CharField(
        max_length=255,
    )
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=11,
    )
    description = RichTextField()
