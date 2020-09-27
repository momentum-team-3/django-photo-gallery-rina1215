from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.decorators import api_view
from photographygal.models import Gallery, Picture
from api.serializers import GallerySerializer, PictureSerializer
from rest_framework import viewsets, permissions, authentication



#@api_view(http_method_names=["GET"])
#def list_gallery(request):
    #gallery =Gallery.objects.for_user(request.user)
    #serializer =GallerySerializer(gallery, many=True)
    #return Response(serializer.data)

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [ permissions.IsAuthenticated ]


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [ permissions.IsAuthenticated ]
