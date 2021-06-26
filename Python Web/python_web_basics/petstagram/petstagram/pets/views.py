from django.shortcuts import render, redirect

from petstagram.pets.forms import CreatePetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def pet_list(req):
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }
    return render(req, 'pet_list.html', context)


def pet_detail(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes = pet.like_set.count()

    context = {
        'pet': pet,
    }

    return render(req, 'pet_detail.html', context)


def like_pet(_, pk):
    pet = Pet.objects.get(pk=pk)

    like = Like(
        pet=pet
    )
    like.save()

    return redirect('pet detail', pk)


def create_pet(req):
    if req.method == "POST":
        form = CreatePetForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('pets list')
    else:
        form = CreatePetForm()

    context = {
        'form': form,
    }

    return render(req, 'pet_create.html', context)


def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == "POST":
        form = EditPetForm(req.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet detail', pk)
    else:
        form = EditPetForm(instance=pet)

    context = {
        'pet': pet,
        'form': form,
    }

    return render(req, 'pet_edit.html', context)


def delete_pet(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == "POST":
        pet.delete()
        return redirect('pets list')

    context = {
        'pet': pet,
    }

    return render(req, 'pet_delete.html', context)
