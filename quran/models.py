from django.db import models
from django_extensions.db.models import TimeStampedModel


class Sureh(TimeStampedModel):
    PUBLISH = (
        ("مکی", "مکی"),
        ("مدینه", "مدینه")
    )
    title = models.CharField(
        max_length=250,
    )
    publish = models.CharField(
        max_length=10,
        choices=PUBLISH,
    )
    meaning = models.CharField(
        max_length=250,
    )
    nozol = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "سوره ها"

    def __str__(self):
        return self.title


class Ayeh(TimeStampedModel):
    HEZEB = [(str(i), i) for i in range(1, 5)]
    JOZE = [(str(i), i) for i in range(1, 31)]
    CHOICE = (
        ("مستحب", "مستحب"),
        ("واجب", "واجب"),
        ("ندارد", "ندارد"),
    )
    title = models.TextField(
        verbose_name="متن",
    )
    sureh = models.ForeignKey(
        Sureh,
        on_delete=models.CASCADE,
        verbose_name="سوره",
    )
    sejdeh = models.CharField(
        max_length=6,
        choices=CHOICE,
        verbose_name="سجده",
    )
    hezb = models.CharField(
        max_length=10,
        choices=HEZEB,
        verbose_name="حزب",
    )
    joze = models.CharField(
        max_length=10,
        choices=JOZE,
        verbose_name="جز",
    )
    page_number = models.PositiveIntegerField(
        verbose_name="شماره صفحه",
    )
    ayeh_number = models.PositiveIntegerField(
        verbose_name="شماره آیه",
    )

    class Meta:
        verbose_name = "ایه"
        verbose_name_plural = "آیه ها"

    def __str__(self):
        return f'{self.sureh} ایه {self.ayeh_number}'
