from django import forms

from notes.notes.models import Note
from utils.mixins.BootstrapMixins import DisableFormMixin


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class CreateNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(DisableFormMixin, NoteForm):
    pass
