from django import forms
from django.core import validators

from .models import Bb, Img


class BbForm(forms.ModelForm):
    image = forms.ImageField(label='Изображение',
                             validators=[validators.FileExtensionValidator(
                                 allowed_extensions=('gif', 'jpg', 'png'))],
                             error_messages={'invalid_extension': 'Этот формат файлов ' + \
                                                                  'не поддерживается'})

    class Meta:
        model = Bb
        fields = ['title', 'image', 'rubric', 'content', 'price']


class ImgForm(forms.ModelForm):
    img = forms.ImageField(label='Изображение',
                           validators=[validators.FileExtensionValidator(
                               allowed_extensions=('gif', 'jpg', 'png'))],
                           error_messages={'invalid_extension': 'Этот формат файлов ' + \
                                                                'не поддерживается'})
    desc = forms.CharField(label='Описание',
                           widget=forms.widgets.Textarea())

    class Meta:
        model = Img
        fields = '__all__'
