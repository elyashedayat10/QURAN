from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel

# Create your models here.
user = get_user_model()


class Note(TimeStampedModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return f'{self.user}-{self.title}'


class Countdown(TimeStampedModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='countdowns')
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user}-{self.title}'
