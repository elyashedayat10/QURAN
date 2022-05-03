from django import forms
from .models import (
    Dirge,
    DirgeCategory,
)
from praiseres.models import Praiser


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
            'name',
            'audio',
            'category',
            'praiser',
        )
        labels = {
            'name': 'نام مداحی',
            'audio': 'فایل صوتی',
            'category': 'دسته بندی',
            'praiser': 'مداح',
        }

    def __init__(self, *args, **kwargs):
        super(DirgeForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'انتخاب کنید'
        self.fields['praiser'].empty_label = 'انتخاب کنید'
        self.fields['*'].error_messages.update({

        })
