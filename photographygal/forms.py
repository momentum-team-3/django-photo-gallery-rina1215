from django import forms
from .models import Gallery, Picture

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            "title",
            "comments",
        ]




class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = [
            "title",
            "comments",


        ]