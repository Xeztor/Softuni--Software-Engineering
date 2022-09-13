from django.urls import path

from notes.notes.views import home, delete_note, create_note, edit_note, note_details

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_note, name='note create'),
    path('edit/<int:pk>', edit_note, name='note edit'),
    path('delete/<int:pk>', delete_note, name='note delete'),
    path('details/<int:pk>', note_details, name='note details'),
]
