
from django import forms
from .models import Gallery, Picture, Comments



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

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'text'
        ]

        