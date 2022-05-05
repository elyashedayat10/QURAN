from django.urls import path
from .views import (
    SliderListView,
    SliderCreateView,
    SliderUpdateView,
    SliderDeleteView,
    SiteSettingListView,
    SiteSettingCreateView,
    SiteSettingUpdateView,
    PanelView,
    ContactUsListView,
    ContactUsDetailView,
    ContactUsDeleteView,
    AboutUsCreateView,
    AboutUsView,
    AboutUsUpdateView,
)

app_name = 'config'
urlpatterns = [
    path('slider/list/', SliderListView.as_view(), name='slider_list'),
    path('slider/create/', SliderCreateView.as_view(), name='slider_create'),
    path('slider/update/<int:slider_id>/', SliderUpdateView.as_view(), name='slider_update'),
    path('slider/delete/<int:slider_id>/', SliderDeleteView.as_view(), name='slider_delete'),
    path('site_setting/', SiteSettingListView.as_view(), name='site_setting'),
    path('site_setting/create/', SiteSettingCreateView.as_view(), name='site_setting_create'),
    path('site_setting_update/<int:site_setting_id>/', SiteSettingUpdateView.as_view(), name='site_setting_update'),
    path('panel/', PanelView.as_view(), name='panel'),
    path('contact_us/', ContactUsListView.as_view(), name='contactus_list'),
    path('contact_us/<int:id>/', ContactUsDetailView.as_view(), name='contactus_detail'),
    path('contact_us/delete/<int:id>/', ContactUsDeleteView.as_view(), name='contactus_delete'),
    path('about_us/create/', AboutUsCreateView.as_view(), name='about_us_create'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('about_us_update/<int:id>', AboutUsUpdateView.as_view(), name='about_us_update'),
]
