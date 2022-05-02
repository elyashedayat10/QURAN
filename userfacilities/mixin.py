from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Note, Countdown


class NoteAccessMixin:
    def dispatch(self, request, note_id, *args, **kwargs):
        note = get_object_or_404(Note, id=note_id)
        if note.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")


class CountdownAccessMixin:
    def dispatch(self, request, note_id, *args, **kwargs):
        countdown = get_object_or_404(Countdown, id=note_id)
        if countdown.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")
