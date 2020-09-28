from django.shortcuts import render
from django.shortcuts import get_object_or_404

from api.serializers import GallerySerializer, PictureSerializer

from rest_framework.views import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, authentication
from rest_framework import generics
from rest_framework.parsers import FileUploadParser

#local
from photographygal.models import Gallery, Picture


#create POST and save gallery if authorized user
class GalleryListView(generics.ListCreateAPIView): 
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()
    @api_view(http_method_names=["POST"])
    def perform_create(self, serializer):
        if request.user.is_authenticated:
            serializer.save(user=self.request.user)

#to GET a gallery and view all of the gallery list, all its fields, title, id, description
class GalleryDetailView (generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = GallerySerializer

    def get_queryset(self):  #I will only see the galleries that the user owns
        return self.user.galleries

    def perform_create(self, serializer): #I will registered users can POST
        serializer.save(user=self.request.user)

#unregistered users can view galleries thumbnails
class GalleryViewSet(viewsets.ModelViewSet): 
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#ONLY authenticated user can view pictures which are in gallery
class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [ permissions.IsAuthenticated ]


#class GalleryImageView(APIView):
    #parser_classes = (FileUploadParser)

    #def put(self, request, pk):
        #image = get_object_or_404(self.request.user.galleries, pk=pk)
        #if 'file' not in request.data:
            #raise ParserError('Empty content')
        #file = request.data['file']
        #gallery = image.save(file.name, file, save=True)
        #return Response(status=status.HTTP_200_OK)