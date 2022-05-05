from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
user = get_user_model()


class Note(TimeStampedModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return f"{self.user}-{self.title}"


class Countdown(TimeStampedModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="countdowns")
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user}-{self.title}"


class SchoolSchedule(TimeStampedModel):
    DAY = (
        ("شنبه", "شنبه"),
        ("یکشنبه", "یکشنبه"),
        ("دوشنبه", "دوشنبه"),
        ("سه شنبه", "سه شنبه"),
        ("چهارشنبه", "چهارشنبه"),
        ("پنجشنبه", "پنجشنبه"),
    )
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="schedules")
    day = models.CharField(max_length=10, choices=DAY)
    first = models.CharField(max_length=10)
    second = models.CharField(max_length=10)
    third = models.CharField(max_length=10)
    fourth = models.CharField(max_length=10)
    fifth = models.CharField(max_length=10)
    sixth = models.CharField(max_length=10)


class QadaPrayer(TimeStampedModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="qadas")
    NAMAZ = (
        ("صبح", "صبح"),
        ("ظهر", "ظهر"),
        ("عصر", "عصر"),
        ("مغرب", "مغرب"),
        ("عشا", "عشا"),
        ("آیات", "آیات"),
    )
    namaz = models.CharField(max_length=10, choices=NAMAZ)
    count = models.PositiveSmallIntegerField()
