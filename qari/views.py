from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from .forms import QariForm, QuranAudioForm
# from quran.models import Ayeh
from .models import Ayeh, Qari, QuranAudio


# Create your views here.

class QariList(ListView):
    model = Qari
    template_name = "qari/list.html"


class QariCreateView(CreateView):
    model = Qari
    form_class = QariForm
    success_url = reverse_lazy("qaris:list")
    template_name = "qari/create.html"


class QariUpdateView(UpdateView):
    model = Qari
    form_class = QariForm
    slug_field = 'id'
    slug_url_kwarg = 'qari_id'
    template_name = "qari/update.html"

    def get_success_url(self):
        pass
        # return reverse('Qaris:detail', arge=[self.kwargs.get('Qari_id')])


class QariDeleteView(View):
    def get(self, *args, **kwargs):
        qari = get_object_or_404(Qari, pk=kwargs.get('qari_id'))
        qari.delete()
        return redirect('qaris:list')
