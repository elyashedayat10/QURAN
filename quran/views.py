from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    redirect,
)
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    View,
)
from .forms import (
    AyehForm,
    SurehForm,
)

from .models import (
    Ayeh,
    Sureh,
)




# sureh views
class SurehListView(ListView):
    model = Sureh
    template_name = "quran/sureh_list.html"
    paginate_by = 25


class SurehCreateView(CreateView):
    model = Sureh
    form_class = SurehForm
    success_url = reverse_lazy("quran:sureh_list")
    template_name = "quran/sureh_create.html"

    def form_valid(self, form):
        messages.success()
        return super(SurehCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(SurehCreateView, self).form_invalid(form)


class SurehUpdateView(UpdateView):
    model = Sureh
    form_class = SurehForm
    success_url = reverse_lazy("quran:sureh_list")
    template_name = "quran/sureh_update.html"
    slug_field = "id"
    slug_url_kwarg = "sureh_id"

    def form_valid(self, form):
        messages.success()
        return super(SurehUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(SurehUpdateView, self).form_invalid(form)


class SurehDeleteView(View):
    def get(self, request, sureh_id):
        sureh_obj = get_object_or_404(Sureh, id=sureh_id)
        sureh_obj.delete()
        messages.success()
        return redirect("quran:sureh_list")


# ayeh views

class AyehListView(ListView):
    model = Ayeh
    template_name = "quran/ayeh_list.html"
    paginate_by = 25


class AyehCreateView(CreateView):
    model = Ayeh
    form_class = AyehForm
    success_url = reverse_lazy("quran:ayeh_create")
    template_name = "quran/ayeh_create.html"

    def form_valid(self, form):
        messages.success()
        return super(AyehCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(AyehCreateView, self).form_invalid(form)


class AyehUpdateView(UpdateView):
    model = Ayeh
    form_class = AyehForm
    success_url = reverse_lazy("quran:ayeh_list")
    template_name = "quran/ayeh_update.html"
    slug_field = "id"
    slug_url_kwarg = "ayeh_id"

    def form_valid(self, form):
        messages.success()
        return super(AyehUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.success()
        return super(AyehUpdateView, self).form_invalid(form)


class AyehDeleteView(View):
    def get(self, request, ayeh_id):
        sureh_obj = get_object_or_404(Sureh, id=ayeh_id)
        sureh_obj.delete()
        messages.success()
        return redirect("quran:ayeh_list")
