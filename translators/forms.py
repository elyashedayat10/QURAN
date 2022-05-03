from django import forms
from django import forms
from .models import (
    Translator,
    QuranTranslateAudio,
)


class QuranTranslateAudioForm(forms.ModelForm):
    class Meta:
        model = QuranTranslateAudio
        fields = (
            "audio",
        )
        labels = {
            "audio": "صوت",
        }


class TranslatorForm(forms.ModelForm):
    class Meta:
        model = Translator
        fields = (
            "first_name",
            "last_name",
            'image',
        )
        labels = {
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            'image': 'تصویر پروفایل',
        }
