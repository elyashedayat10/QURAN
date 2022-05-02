from django.urls import path
from .views import (
    UserNoteList,
    NoteDetail,
    NoteCreate,
    NoteUpdate,
    NoteDeleteView,

)

app_name = 'facilities'
urlpatterns = [
    path('user_note/', UserNoteList.as_view(), name='user_note'),
    path('note_detail/<int:note_id>/', NoteDetail.as_view(), name='note_detail'),
    path('note_create/', NoteCreate.as_view(), name='note_create'),
    path('note_delete/<int:note_id>/', NoteDeleteView.as_view(), name='note_delete'),
    path('note_update/<int:note_id>/', NoteUpdate.as_view(), name='note_update'),
]
