from django import forms

from praiseres.models import Praiser

from .models import Natal, NatalCategory


class NatalCategoryForm(forms.ModelForm):
    class Meta:
        model = NatalCategory
        fields = (
            'title',
            'logo',
        )
        labels = {
            "title": "عنوان دسته بندی",
            'logo': 'لوگو',
        }


class NatalForm(forms.ModelForm):
    class Meta:
        model = Natal
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
