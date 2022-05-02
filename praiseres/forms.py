from django import forms
from .models import Praiser


class PraiserForm(forms.ModelForm):
    class Meta:
        model = Praiser
        fields = (
            "name",
            "family",
            'image',
        )
        labels = {
            "name": "نام",
            'family': "نام خانوادگی",
            "image": "تصویر",
        }
