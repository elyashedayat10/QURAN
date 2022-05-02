from django.shortcuts import (
    get_object_or_404,
    redirect,
)
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    View,
)
from django.urls import reverse_lazy
from .models import Praiser
from .forms import PraiserForm


# Create your views here.
class PraiserListView(ListView):
    model = Praiser
    template_name = 'praiseres/list.html'


class PraiserCreateView(CreateView):
    model = Praiser
    template_name = 'praiseres/create.html'
    form_class = PraiserForm
    success_url = reverse_lazy("praiseres:list")

    def form_invalid(self, form):
        print(form.errors)
        return super(PraiserCreateView, self).form_invalid(form)


class PraiserUpdateView(UpdateView):
    slug_field = 'name'
    slug_url_kwarg = 'name'
    success_url = reverse_lazy("praiseres:list")
    template_name = 'praiseres/update.html'
    model = Praiser
    form_class = PraiserForm


class PraiserDeleteView(View):
    def get(self, request, name):
        praiser_obj = get_object_or_404(Praiser, name=name)
        praiser_obj.delete()
        return redirect("praiseres:list")
