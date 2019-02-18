from django import forms
from . import models

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )


class UploaderForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['img', 'tags']


class ImageTagEditForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ["tags", ]
