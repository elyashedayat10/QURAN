from django import forms

from .models import (
    Sureh,
    Ayeh,
)


class SurehForm(forms.ModelForm):
    class Meta:
        model = Sureh
        fields = (
            "title",
            "publish",
            "meaning",
            "nozol",
        )

        labels = {
            "title": "نام سوره",
            "publish": "محل نزول",
            "meaning": "معنی نام سوره",
            "nozol": "شماره نزول"
        }


class AyehForm(forms.ModelForm):
    class Meta:
        model = Ayeh
        fields = (
            "title",
            'sureh',
            'page_number',
            'sejdeh',
            "hezb",
            "joze",
            "ayeh_number",
        )
        labels = {
            "title": "متن",
            "sureh": "سوره",
            "sejdeh": "سجده",
            "hezb": "حزب",
            "ayeh_number": "شماره آیه",
            "joze": "جز",
            "page_number": "شماره صفحه"
        }
