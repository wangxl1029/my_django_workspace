from django import forms


class UploaderForm(forms.Form):
    img = forms.ImageField()
