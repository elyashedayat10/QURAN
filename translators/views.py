from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    View,
)
from django.urls import reverse_lazy
from .models import (
    Translator,
    QuranTranslateAudio,
)
from .forms import (
    QuranTranslateAudio,
    TranslatorForm,
)
# from quran.models import Ayeh
from .models import Ayeh


# Create your views here.

class TranslatorList(ListView):
    model = Translator
    template_name = "translators/list.html"


class TranslatorCreateView(CreateView):
    model = Translator
    form_class = TranslatorForm
    success_url = reverse_lazy("translators:list")
    template_name = "translators/create.html"


class TranslatorUpdateView(UpdateView):
    model = Translator
    form_class = TranslatorForm
    slug_field = 'id'
    slug_url_kwarg = 'translator_id'
    template_name = "translators/update.html"

    def get_success_url(self):
        pass
        # return reverse('translators:detail', arge=[self.kwargs.get('translator_id')])


class TranslatorDeleteView(View):
    def get(self, *args, **kwargs):
        translator = get_object_or_404(Translator, pk=kwargs.get('Translator_id'))
        translator.delete()
        return redirect('translators:list')
