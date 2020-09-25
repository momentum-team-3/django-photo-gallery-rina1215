
from django import forms
from .models import Gallery, Picture

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            #"user",
            "title",
            "description",
            "image",
            #"thumbnail",
            
            
            
        ]




class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = [
            "title",
            "description",
            "image",
            "gallery"


        ]
