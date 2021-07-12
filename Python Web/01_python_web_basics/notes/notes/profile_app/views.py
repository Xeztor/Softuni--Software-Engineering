from django.shortcuts import render, redirect

from notes.notes.models import Note
from utils.profile_app import get_profile


def profile_details(req):
    profile = get_profile()
    notes_count = Note.objects.all().count()
    context = {
        'profile': profile,
        'notes_count': notes_count
    }
    return render(req, 'profile_app/profile.html', context)


def delete_profile(_):
    profile = get_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home')
