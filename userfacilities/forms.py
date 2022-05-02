from django import forms
from .models import Note, Countdown


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'description',
        )
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات',
        }


class CountdownForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'description',
            'start_time',
        )
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات',
            'start_time': 'زمان شروع',
        }
