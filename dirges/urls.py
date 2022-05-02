from django.urls import path

from .views import (
    DirgeCategoryListView,
    DirgeCategoryDetailView,
    DirgeCategoryCreate,
    DirgeCategoryUpdate,
    DirgeCategoryDelete,
    DirgeListView,
    DirgeCreateView,
    DirgeUpdateView,
    DirgeDeleteView,
)

app_name = 'dirges'

urlpatterns = [
    path('category_list/', DirgeCategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:category_id>/', DirgeCategoryDetailView.as_view(), name='category_detail'),
    path('category_update/<int:category_id>/', DirgeCategoryUpdate.as_view(), name='category_update'),
    path('category_delete/<int:category_id>/', DirgeCategoryDelete.as_view(), name='category_delete'),
    path('category_create/', DirgeCategoryCreate.as_view(), name='category_create'),
    path('list/', DirgeListView.as_view(), name='list'),
    path('create/', DirgeCreateView.as_view(), name='create'),
    path('update/<int:dirge_id>/', DirgeUpdateView.as_view(), name='update'),
    path('delete/<int:dirge_id>/', DirgeDeleteView.as_view(), name='delete'),
]
