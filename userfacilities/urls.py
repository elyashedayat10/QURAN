from django.urls import path

from .views import (
    CountdownCreate,
    CountdownDeleteView,
    CountdownDetail,
    CountdownUpdate,
    NoteCreate,
    NoteDeleteView,
    NoteDetail,
    NoteUpdate,
    ScheduleCreate,
    ScheduleDeleteView,
    ScheduleUpdate,
    UserCountdownList,
    UserNoteList,
    UserScheduleList,
)

app_name = "facilities"
urlpatterns = [
    path("user_note/", UserNoteList.as_view(), name="user_note"),
    path("note_detail/<int:note_id>/", NoteDetail.as_view(), name="note_detail"),
    path("note_create/", NoteCreate.as_view(), name="note_create"),
    path("note_delete/<int:note_id>/", NoteDeleteView.as_view(), name="note_delete"),
    path("note_update/<int:note_id>/", NoteUpdate.as_view(), name="note_update"),
    path("user_countdown/", UserCountdownList.as_view(), name="user_countdown"),
    path(
        "countdown_detail/<int:countdown_id>/",
        CountdownDetail.as_view(),
        name="countdown_detail",
    ),
    path("countdown_create/", CountdownCreate.as_view(), name="countdown_create"),
    path(
        "countdown_delete/<int:countdown_id>/",
        CountdownDeleteView.as_view(),
        name="countdown_delete",
    ),
    path(
        "countdown_update/<int:countdown_id>/",
        CountdownUpdate.as_view(),
        name="countdown_update",
    ),
    path("user_schedule/", UserScheduleList.as_view(), name="user_schedule"),
    # path('schedule_detail/<int:schedule_id>/', S.as_view(), name='schedule_detail'),
    path("schedule_create/", ScheduleCreate.as_view(), name="schedule_create"),
    path(
        "schedule_delete/<int:schedule_id>/",
        ScheduleDeleteView.as_view(),
        name="schedule_delete",
    ),
    path(
        "schedule_update/<int:schedule_id>/",
        ScheduleUpdate.as_view(),
        name="schedule_update",
    ),
]
