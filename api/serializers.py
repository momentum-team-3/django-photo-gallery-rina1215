from photographygal.models import Gallery, Picture
from rest_framework import serializers
from users.models import User


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = [ 
            "title",
            "description",
            "image",
            'id'
        ]



class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = [
            "title",
            "description",
            "image",
            "gallery",
            "id"
        ]

