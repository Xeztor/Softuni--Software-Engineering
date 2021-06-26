from django import forms

from expenses.profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class RegisterForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass
