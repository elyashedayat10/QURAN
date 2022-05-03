from django.urls import path
from .views import (
    SurehListView,
    SurehUpdateView,
    SurehDeleteView,
    SurehCreateView,
    AyehUpdateView,
    AyehListView,
    AyehCreateView,
    AyehDeleteView,
)

app_name = 'quran'

urlpatterns = [
    path('sureh_list/', SurehListView.as_view(), name='sureh_list'),
    path('sureh_update/<int:sureh_id>/', SurehUpdateView.as_view(), name='sureh_update'),
    path('sureh_create/', SurehCreateView.as_view(), name='sureh_create'),
    path('sureh_delete/<int:sureh_id>/', SurehDeleteView.as_view(), name='sureh_delete'),
    path('ayeh_list/', AyehListView.as_view(), name='ayeh_list'),
    path('ayeh_create/', AyehCreateView.as_view(), name='ayeh_create'),
    path('ayeh_update/<int:ayeh_id>/', AyehUpdateView.as_view(), name='ayeh_update'),
    path('ayeh_delete/<int:ayeh_id>/', AyehDeleteView.as_view(), name='ayeh_delete'),
]
