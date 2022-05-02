from django.shortcuts import (
    get_object_or_404,
    redirect,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView,
    CreateView,
    View,
)
from .models import (
    Natal,
    NatalCategory,
)
from .forms import (
    NatalForm,
    NatalCategoryForm,
)


# Create your views here.

class NatalCategoryListView(ListView):
    model = NatalCategory
    template_name = "natals/natal_category_list.html"


class NatalCategoryDetailView(DetailView):
    model = NatalCategory
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "natals/natal_category_detail.html"


class NatalCategoryCreate(CreateView):
    model = NatalCategory
    template_name = 'natals/natal_category_create.html'
    form_class = NatalCategoryForm
    success_url = reverse_lazy("natals:Natal_category_list")


class NatalCategoryUpdate(UpdateView):
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy("natals:category_list")
    template_name = 'natals/natal_category_update.html'
    model = NatalCategory
    form_class = NatalCategoryForm


class NatalCategoryDelete(View):
    def get(self, request, slug):
        Natal_category_obj = get_object_or_404(NatalCategory, slug=slug)
        Natal_category_obj.delete()
        return redirect("natals:Natal_category_list")


class NatalListView(ListView):
    model = Natal
    template_name = "natals/natal_list.html"


class NatalCreateView(CreateView):
    model = Natal
    form_class = NatalForm
    success_url = reverse_lazy("natals:list")
    template_name = "natals/natal_create.html"


class NatalUpdateView(UpdateView):
    model = Natal
    form_class = NatalForm
    # success_url = reverse_lazy("natals:Molody_List")
    template_name = "natals/natal_update.html"
    slug_field = "song_name"
    slug_url_kwarg = "song_name"


class NatalDeleteView(View):
    def get(self, request, song_name):
        Natal_obj = get_object_or_404(Natal, song_name=song_name)
        Natal_obj.delete()
        return redirect("natals:list")
