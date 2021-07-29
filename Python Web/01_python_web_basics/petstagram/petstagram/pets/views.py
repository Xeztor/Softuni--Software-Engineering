from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import CreatePetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def pet_list(request):
    pets = Pet.objects.all()
    context = {
        'page_name': 'list_page',
        'pets': pets
    }
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes = pet.like_set.count()

    comments = Comment.objects.all()
    context = {
        'page_name': 'detail_page',
        'pet': pet,
        'comment_form': CommentForm(),
        'comments': comments,
    }

    return render(request, 'pet_detail.html', context)


def like_pet(_, pk):
    pet = Pet.objects.get(pk=pk)

    like = Like(
        pet=pet
    )
    like.save()

    return redirect('pet detail', pk)


def create_pet(request):
    if request.method == "POST":
        form = CreatePetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pets list')
    else:
        form = CreatePetForm()

    context = {
        'page_name': 'create_page',
        'form': form,
    }

    return render(request, 'pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == "POST":
        form = EditPetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet detail', pk)
    else:
        form = EditPetForm(instance=pet)

    context = {
        'page_name': 'edit_page',
        'pet': pet,
        'form': form,
    }

    return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == "POST":
        pet.delete()
        return redirect('pets list')

    context = {
        'page_name': 'delete_page',
        'pet': pet,
    }

    return render(request, 'pet_delete.html', context)
