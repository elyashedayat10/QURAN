from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    View,
    DetailView,
)
from django.urls import reverse_lazy
from .models import (
    Slider,
    SiteSetting,
    ContactUS,
    AboutUs,
)
from .forms import (
    SliderForm,
    SiteSettingForm,
    ContactUsForm,
    AboutUsForm,
)


# from utils import IsAdminUserMixin


# Create your views here.


# slider views

class SliderListView(ListView):
    model = Slider
    template_name = 'config/slider_list.html'
    context_object_name = 'slider_list'

    def get_context_data(self, **kwargs):
        context_data = super(SliderListView, self).get_context_data(**kwargs)
        context_data['slider_count'] = Slider.objects.count()
        return context_data


class SliderCreateView(CreateView):
    model = Slider
    template_name = 'config/slider_create.html'
    form_class = SliderForm
    success_url = reverse_lazy('config:slider_list')

    def form_valid(self, form):
        messages.success(self.request, '', '')
        return super(SliderCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', '')
        return super(SliderCreateView, self).form_invalid(form)


class SliderUpdateView(UpdateView):
    model = Slider
    template_name = 'config/slider_update.html'
    form_class = SliderForm
    success_url = reverse_lazy('config:slider_list')
    slug_field = 'id'
    slug_url_kwarg = 'slider_id'

    def form_valid(self, form):
        messages.success(self.request, '', '')
        return super(SliderUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', '')
        return super(SliderUpdateView, self).form_invalid(form)


class SliderDeleteView(View):
    def get(self, request, slider_id):
        slider_obj = get_object_or_404(Slider, id=slider_id)
        slider_obj.delete()
        messages.success(request, '', '')
        return redirect('config:slider_list')


# site setting  views
class SiteSettingListView(View):
    def get(self, request):
        site_setting_obj = SiteSetting.objects.first()
        return render(request, 'config/site_setting_list.html', {'object': site_setting_obj})


class SiteSettingCreateView(CreateView):
    model = SiteSetting
    template_name = 'config/site_setting_create.html'
    form_class = SiteSettingForm
    success_url = reverse_lazy("config:site_setting")

    def form_valid(self, form):
        # messages.success()
        return super(SiteSettingCreateView, self).form_valid(form)

    def form_invalid(self, form):
        # messages.error()
        return super(SiteSettingCreateView, self).form_invalid(form)


class SiteSettingUpdateView(UpdateView):
    model = SiteSetting
    template_name = 'config/site_setting_update.html'
    form_class = SiteSettingForm
    success_url = reverse_lazy('config:site_setting')
    slug_field = 'id'
    slug_url_kwarg = 'site_setting_id'

    def form_valid(self, form):
        messages.success()
        return super(SiteSettingUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(SiteSettingUpdateView, self).form_invalid(form)


class PanelView(View):
    def get(self, request):
        return render(request, 'config/panel.html')


class SiteHome(View):
    def get(self, request):
        return render(request, '', '')


class ContactUsCreateView(CreateView):
    model = ContactUS
    form_class = ContactUsForm
    template_name = 'config/contactus_create.html'


class ContactUsListView(ListView):
    model = ContactUS
    template_name = 'config/contactus.html'


class ContactUsDetailView(DetailView):
    model = ContactUS
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'config/contactus_detail.html'


class ContactUsDeleteView(View):
    def get(self, request, id):
        contact_obj = get_object_or_404(ContactUS, id=id)
        contact_obj.delete()
        messages.success(request, '', '')
        return redirect("config:contactus_list")


class AboutUsCreateView(CreateView):
    model = AboutUs
    form_class = AboutUsForm
    template_name = 'config/aboutus_create.html'
    success_url = reverse_lazy('config:about_us')


class AboutUsView(View):
    def get(self, request):
        about_us_obj = AboutUs.objects.first()
        return render(request, 'config/aboutus.html', {"object": about_us_obj})


class AboutUsUpdateView(UpdateView):
    model = AboutUs
    template_name = 'config/site_setting_update.html'
    form_class = AboutUsForm
    success_url = reverse_lazy('config:about_us')
    slug_field = 'id'
    slug_url_kwarg = 'id'
