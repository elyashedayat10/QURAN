from django.urls import path

from .views import QariCreateView, QariDeleteView, QariList, QariUpdateView

app_name = 'qaris'
urlpatterns = [
    path('list/', QariList.as_view(), name='list'),
    path('create/', QariCreateView.as_view(), name='create'),
    path('update/<int:qari_id>/', QariUpdateView.as_view(), name='update'),
    path('delete/<int:qari_id>/', QariDeleteView.as_view(), name='delete'),

]
