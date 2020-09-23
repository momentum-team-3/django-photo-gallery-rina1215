
from django import forms
from .models import Gallery, Picture

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            #"creator"
            "name",
            "description",
            "image",
            
            
            
        ]




class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = [
            "name",
            "description",
            "image",


        ]
