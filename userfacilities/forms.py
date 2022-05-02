from django import forms

from .models import Countdown, Note, SchoolSchedule


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
            "description",
            "start_time",
        )
        labels = {
            "title": "عنوان",
            "description": "توضیحات",
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
