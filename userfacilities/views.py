from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import CountdownForm, NoteForm, SchoolScheduleForm
from .mixin import CountdownAccessMixin, NoteAccessMixin, ScheduleAccessMixin
from .models import Countdown, Note, SchoolSchedule


# Create your views here.
class UserNoteList(ListView):
    template_name = "facilities/user_notes_list.html"

    def get_queryset(self):
        notes = Note.objects.filter(user=self.request.user)
        return notes


class NoteDetail(NoteAccessMixin, DetailView):
    model = Note
    slug_field = "id"
    slug_url_kwarg = "note_id"
    template_name = "facilities/user_note_detail.html"


class NoteCreate(CreateView):
    model = Note
    form_class = Note
    template_name = "facilities/user_note_create.html"
    success_url = reverse_lazy("facilities:user_note")

    def form_valid(self, form):
        new_note = form.save(commit=False)
        new_note.user = self.request.user
        new_note.save()
        messages.success()
        return super(NoteCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(NoteCreate, self).form_invalid(form)


class NoteUpdate(NoteAccessMixin, UpdateView):
    model = Note
    slug_field = "id"
    slug_url_kwarg = "note_id"
    template_name = "facilities/user_note_update.html"
    form_class = NoteForm

    def get_success_url(self):
        return reverse("facilities:note_detail", args=[self.kwargs.get("note_id")])

    def form_valid(self, form):
        messages.success()
        return super(NoteUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(NoteUpdate, self).form_invalid(form)


class NoteDeleteView(NoteAccessMixin, View):
    def get(self, note_id):
        note = get_object_or_404(Note, note_id=note_id)
        note.delete()
        messages.success()
        return redirect("facilities:user_note")


# countdown
class UserCountdownList(ListView):
    template_name = "facilities/user_countdown_list.html"

    def get_queryset(self):
        Countdowns = Countdown.objects.filter(user=self.request.user)
        return Countdowns


class CountdownDetail(CountdownAccessMixin, DetailView):
    model = Countdown
    slug_field = "id"
    slug_url_kwarg = "countdown_id"
    template_name = "facilities/countdown_detail.html"


class CountdownCreate(CreateView):
    model = Countdown
    form_class = CountdownForm
    template_name = "facilities/count_down_create.html"
    success_url = reverse_lazy("facilities:user_countdown")


class CountdownUpdate(CountdownAccessMixin, UpdateView):
    model = Countdown
    slug_field = "id"
    slug_url_kwarg = "countdown_id"
    template_name = "facilities/countdown_update.html"
    form_class = CountdownForm

    def get_success_url(self):
        return reverse(
            "facilities:countdown_detail", args=[self.kwargs.get("countdown_id")]
        )


class CountdownDeleteView(CountdownAccessMixin, View):
    def get(self, Countdown_id):
        countdown = get_object_or_404(Countdown, Countdown_id=Countdown_id)
        countdown.delete()
        messages.success()
        return redirect("facilities:user_countdown")


# schedule
class UserScheduleList(ListView):
    template_name = "facilities/user_schedule_list.html"

    def get_queryset(self):
        user_schedule = SchoolSchedule.objects.filter(user=self.request.user)
        return user_schedule


class ScheduleUpdate(ScheduleAccessMixin, UpdateView):
    model = SchoolSchedule
    slug_field = "id"
    slug_url_kwarg = "schedule_id"
    template_name = "facilities/schedule_update.html"
    success_url = reverse_lazy("facilities:user_schedule")
    form_class = SchoolScheduleForm


class ScheduleDeleteView(ScheduleAccessMixin, View):
    def get(self, schedule_id):
        schedule_obj = get_object_or_404(SchoolSchedule, id=schedule_id)
        schedule_obj.delete()
        messages.success()
        return redirect("facilities:user_schedule")


class ScheduleCreate(CreateView):
    model = SchoolSchedule
    form_class = SchoolScheduleForm
    template_name = "facilities/schedule_create.html"
    success_url = reverse_lazy("facilities:user_schedule")
