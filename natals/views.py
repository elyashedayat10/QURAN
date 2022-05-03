from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from .forms import NatalCategoryForm, NatalForm
from .models import Natal, NatalCategory

# Create your views here.

class NatalCategoryListView(ListView):
    model = NatalCategory
    template_name = "natals/category_list.html"


class NatalCategoryDetailView(DetailView):
    model = NatalCategory
    slug_field = "id"
    slug_url_kwarg = "category_id"
    template_name = "natals/category_detail.html"


class NatalCategoryCreate(CreateView):
    model = NatalCategory
    template_name = 'natals/category_create.html'
    form_class = NatalCategoryForm
    success_url = reverse_lazy("natals:category_list")


class NatalCategoryUpdate(UpdateView):
    slug_field = 'id'
    slug_url_kwarg = 'category_id'
    template_name = 'natals/category_update.html'
    model = NatalCategory
    form_class = NatalCategoryForm

    def get_success_url(self):
        return reverse('natals:category_detail', args=[self.kwargs.get('category_id')])


class NatalCategoryDelete(View):
    def get(self, request, slug):
        Natal_category_obj = get_object_or_404(NatalCategory, slug=slug)
        Natal_category_obj.delete()
        return redirect("natals:category_list")


class NatalListView(ListView):
    model = Natal
    template_name = "natals/list.html"


class NatalCreateView(CreateView):
    model = Natal
    form_class = NatalForm
    success_url = reverse_lazy("natals:list")
    template_name = "natals/create.html"


class NatalUpdateView(UpdateView):
    model = Natal
    form_class = NatalForm
    template_name = "natals/update.html"
    slug_field = "id"
    slug_url_kwarg = "natal_id"

    def get_success_url(self):
        return reverse("natals:detail", args=[self.kwargs.get('Natal_id')])


class NatalDetailView(DetailView):
    model = Natal
    template_name = 'natals/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'natal_id'


class NatalDeleteView(View):
    def get(self, request, song_name):
        Natal_obj = get_object_or_404(Natal, song_name=song_name)
        Natal_obj.delete()
        return redirect("natals:list")
