from django.urls import path

from .views import (
    NatalCategoryListView,
    NatalCategoryDetailView,
    NatalCategoryCreate,
    NatalCategoryUpdate,
    NatalCategoryDelete,
    NatalListView,
    NatalCreateView,
    NatalUpdateView,
    NatalDeleteView,
)

app_name = 'natals'

urlpatterns = [
    path('category_list/', NatalCategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:category_id>/', NatalCategoryDetailView.as_view(), name='category_detail'),
    path('category_update/<int:category_id>/', NatalCategoryUpdate.as_view(), name='category_update'),
    path('category_delete/<int:category_id>/', NatalCategoryDelete.as_view(), name='category_delete'),
    path('category_create/', NatalCategoryCreate.as_view(), name='category_create'),
    path('list/', NatalListView.as_view(), name='list'),
    path('create/', NatalCreateView.as_view(), name='create'),
    path('update/<int:Natal_id>/', NatalUpdateView.as_view(), name='update'),
    path('delete/<int:Natal_id>/', NatalDeleteView.as_view(), name='delete'),
]
