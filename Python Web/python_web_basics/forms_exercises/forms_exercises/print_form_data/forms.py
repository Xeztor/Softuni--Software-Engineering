from django import forms


class DataForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(
        widget=forms.NumberInput(),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    text = forms.CharField(
        widget=forms.Textarea,
    )