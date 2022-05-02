from django import forms
from .models import (
    Dirge,
    DirgeCategory,
)


class DirgeCategoryForm(forms.ModelForm):
    class Meta:
        model = DirgeCategory
        fields = (
            'title',
            'logo',
        )
        labels = {
            "title": "عنوان دسته بندی",
            'logo': 'لوگو',
        }


class DirgeForm(forms.ModelForm):
    class Meta:
        model = Dirge
        fields = (
            'category',
            'dirge_name',
            'audio',
            'praiser',
        )
        labels = {
            'category': 'دسته بندی',
            'dirge_name': 'نام مولودی',
            'audio': 'فایل صوتی',
            'singer': 'خواننده',
        }
