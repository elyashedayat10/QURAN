from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from .forms import DirgeCategoryForm, DirgeForm
from .models import Dirge, DirgeCategory

# Create your views here.

class DirgeCategoryListView(ListView):
    model = DirgeCategory
    template_name = "dirges/category_list.html"


class DirgeCategoryDetailView(DetailView):
    model = DirgeCategory
    slug_field = "id"
    slug_url_kwarg = "category_id"
    template_name = "dirges/category_detail.html"


class DirgeCategoryCreate(CreateView):
    model = DirgeCategory
    template_name = 'dirges/category_create.html'
    form_class = DirgeCategoryForm
    success_url = reverse_lazy("dirges:category_list")


class DirgeCategoryUpdate(UpdateView):
    slug_field = 'id'
    slug_url_kwarg = 'category_id'
    template_name = 'dirges/category_update.html'
    model = DirgeCategory
    form_class = DirgeCategoryForm

    def get_success_url(self):
        return reverse('dirges:category_detail', args=[self.kwargs.get('category_id')])


class DirgeCategoryDelete(View):
    def get(self, request, slug):
        dirge_category_obj = get_object_or_404(DirgeCategory, slug=slug)
        dirge_category_obj.delete()
        return redirect("dirges:category_list:")


class DirgeListView(ListView):
    model = Dirge
    template_name = "dirges/list.html"


class DirgeCreateView(CreateView):
    model = Dirge
    form_class = DirgeForm
    success_url = reverse_lazy("dirges:list")
    template_name = "dirges/create.html"


class DirgeUpdateView(UpdateView):
    model = Dirge
    form_class = DirgeForm
    template_name = "dirges/update.html"
    slug_field = "id"
    slug_url_kwarg = "dirge_id"

    def get_success_url(self):
        return reverse("dirges:detail", args=[self.kwargs.get('dirge_id')])


class DirgeDetailView(DetailView):
    model = Dirge
    template_name = 'dirges/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'dirge_id'


class DirgeDeleteView(View):
    def get(self, request, song_name):
        dirge_obj = get_object_or_404(Dirge, song_name=song_name)
        dirge_obj.delete()
        return redirect("dirges:list")
