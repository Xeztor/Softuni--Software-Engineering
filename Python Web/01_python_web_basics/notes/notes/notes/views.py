from django.shortcuts import render, redirect

from notes.notes.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes.profile_app.forms import CreateProfileForm
from notes.notes.models import Note
from utils.profile_app import get_profile


def create_profile(req):
    if req.method == "POST":
        form = CreateProfileForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(req, 'home-no-profile.html', context)


def home(req):
    profile = get_profile()
    if not profile:
        return create_profile(req)

    notes = Note.objects.all()
    context = {
        'notes': notes,
    }

    return render(req, 'home-with-profile.html', context)


def create_note(req):
    if req.method == "POST":
        form = CreateNoteForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(req, 'note-create.html', context)


def edit_note(req, pk):
    note = Note.objects.get(pk=pk)
    if req.method == "POST":
        form = EditNoteForm(req.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(req, 'note-edit.html', context)


def delete_note(req, pk):
    note = Note.objects.get(pk=pk)
    if req.method == "POST":
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(req, 'note-delete.html', context)


def note_details(req, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }
    return render(req, 'note-details.html', context)
