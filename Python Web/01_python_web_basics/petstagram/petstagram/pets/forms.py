from django import forms

from petstagram.mixins.BootstrapMixins import FormControlMixin
from petstagram.pets.models import Pet


class PetForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class CreatePetForm(PetForm):
    pass


class EditPetForm(CreatePetForm):
    pass
