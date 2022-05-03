from django.urls import path
from .views import (
    TranslatorList,
    TranslatorCreateView,
    TranslatorUpdateView,
    TranslatorDeleteView,
)

app_name = 'translators'
urlpatterns = [
    path('list/', TranslatorList.as_view(), name='list'),
    path('create/', TranslatorCreateView.as_view(), name='create'),
    path('update/<int:translator_id>/', TranslatorUpdateView.as_view(), name='update'),
    path('delete/<int:translator_id>/', TranslatorDeleteView.as_view(), name='delete'),

]
