from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Note


class NoteAccessMixin:
    def dispatch(self, request, note_id, *args, **kwargs):
        article = get_object_or_404(Note, id=note_id)
        if article.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")
