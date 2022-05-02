from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Countdown, Note, SchoolSchedule


class NoteAccessMixin:
    def dispatch(self, request, note_id, *args, **kwargs):
        note = get_object_or_404(Note, id=note_id)
        if note.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")


class CountdownAccessMixin:
    def dispatch(self, request, count_id, *args, **kwargs):
        countdown = get_object_or_404(Countdown, id=count_id)
        if countdown.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")


class ScheduleAccessMixin:
    def dispatch(self, request, schedule_id, *args, **kwargs):
        countdown = get_object_or_404(SchoolSchedule, id=schedule_id)
        if countdown.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")
