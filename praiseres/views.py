from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from .forms import PraiserForm
from .models import Praiser


# Create your views here.
class PraiserListView(ListView):
    model = Praiser
    template_name = 'praiseres/list.html'


class PraiserCreateView(CreateView):
    model = Praiser
    template_name = 'praiseres/create.html'
    form_class = PraiserForm
    success_url = reverse_lazy("praiseres:list")


class PraiserUpdateView(UpdateView):
    slug_field = 'id'
    slug_url_kwarg = 'praiser_id'
    success_url = reverse_lazy("praiseres:list")
    template_name = 'praiseres/update.html'
    model = Praiser
    form_class = PraiserForm


class PraiserDeleteView(View):
    def get(self, request, praiser_id):
        praiser_obj = get_object_or_404(Praiser, name=praiser_id)
        praiser_obj.delete()
        return redirect("praiseres:list")


class PraiserDetail(DetailView):
    slug_field = 'id'
    slug_url_kwarg = 'praiser_id'
    template_name = 'praiseres/detail.html'
    model = Praiser
