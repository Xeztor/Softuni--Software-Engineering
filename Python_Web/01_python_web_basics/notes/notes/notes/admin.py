from django.contrib import admin

from notes.notes.models import Note


@admin.register(Note)
class TodoNote(admin.ModelAdmin):
    pass