from django import forms

from .models import Qari, QuranAudio


class QuranAudioForm(forms.ModelForm):
    class Meta:
        model = QuranAudio
        fields = (
            "audio",
        )
        labels = {
            "audio": "صوت",
        }


class QariForm(forms.ModelForm):
    class Meta:
        model = Qari
        fields = (
            "first_name",
            "last_name",
        )
        labels = {
            "first_name": "نام",
            "last_name": "نام خانوادگی",
        }
