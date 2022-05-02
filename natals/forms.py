from django import forms
from .models import (
    Natal,
    NatalCategory,
)


class NatalCategoryForm(forms.ModelForm):
    class Meta:
        model = NatalCategory
        fields = (
            'title',
        )
        labels = {
            "title": "عنوان دسته بندی",
        }


class NatalForm(forms.ModelForm):
    class Meta:
        model = Natal
        fields = (
            'category',
            'natal_name',
            'audio',
            'praiser',
        )
        labels = {
            'category': 'دسته بندی',
            'natal_name': 'نام مولودی',
            'audio': 'فایل صوتی',
            'praiser': 'خواننده',
        }
