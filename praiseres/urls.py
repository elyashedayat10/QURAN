from django.urls import path

from .views import (PraiserCreateView, PraiserDeleteView, PraiserDetail,
                    PraiserListView, PraiserUpdateView)

app_name = 'Paraiser'

urlpatterns = [
    path('list/', PraiserListView.as_view(), name='list'),
    path('create/', PraiserCreateView.as_view(), name='create'),
    path('update/<int:praiser_id>/', PraiserUpdateView.as_view(), name='update'),
    path('delete/<int:praiser_id>/', PraiserDeleteView.as_view(), name='delete'),
    path('detail/<int:praiser_id>/', PraiserDetail.as_view(), name='detail'),
]
