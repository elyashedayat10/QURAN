from django import forms
from .models import (
    Slider,
    SiteSetting,
    ContactUS,
    AboutUs,
)


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            'title',
            'image',
        )
        labels = {
            'title': 'عنوان',
            'image': 'تصویر',
        }


class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = (
            'title',
            'image',
        )
        labels = {
            'title': 'عنوان',
            'image': 'تصویر'
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = (
            'full_name',
            'title',
            'email',
            'phone_number',
            'description',
        )
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'title': 'موضوع',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'description': 'توضیحات',
        }


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = (
            'title',
            'description',
        )
        labels = {
            'title': 'عنوان',
            'description': 'متن درباره ما',
        }
