from django import forms

from .models import Countdown, Note, QadaPrayer, SchoolSchedule


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            "title",
            "description",
        )
        labels = {
            "title": "عنوان",
            "description": "توضیحات",
        }


class CountdownForm(forms.ModelForm):
    class Meta:
        model = Countdown
        fields = (
            "title",
            "start_time",
        )
        labels = {
            "title": "عنوان",
            "start_time": "زمان شروع",
        }


class SchoolScheduleForm(forms.ModelForm):
    class Meta:
        model = SchoolSchedule
        fields = (
            "day",
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
        )
        labels = {
            "day": "روز",
            "first": "زنگ اول",
            "second": "زنگ دوم",
            "third": "زنگ سوم",
            "fourth": "زنگ چهارم",
            "fifth": "زنگ پنجم",
            "sixth": "زنگ ششم",
        }


class QadaForm(forms.ModelForm):
    class Meta:
        model = QadaPrayer
        fields = (
            "namaz",
            "count",
        )
