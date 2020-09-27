
from django.shortcuts import render, redirect, get_object_or_404
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from django.views import View
from .models import Gallery, Picture
from .forms import  GalleryForm, PictureForm




def homepage(request):
    return render(request, "photographygal/homepage.html")
    

#this function is rendering my gallery form, my html template, it is getting
#information from user to upload a picture that will have a title and description,
#if it all fits the fields requirements then the information on the form will be saved
#and you will be redirected to a url that has all the galleries thumbnails, descriptions, titles
#QUESTION I DO NOT KNOW HOW TO MAKE EA UPLOADED PICTURE AN URL TO STORE MORE PICTURES
#QUESTION WHERE DOES THE REGULAR SIZE PICTURE GOES TO BEFORE IT GETS PROCESSED? Does it upload to my /media/gallery?
def add_gallery(request):
    if request.method == 'GET':
        form =GalleryForm()
    else:
        form=GalleryForm(data=request.POST, files=request.FILES) #accept data from db and any files to download
        if form. is_valid():
            form.save()
            return redirect (to='list_gallery')
    return render (request, "photographygal/add_galleries.html", {'form':form})

#this will list all the pictures uploaded by the user from gallery form
def list_gallery (request):
    galleries = Gallery.objects.all()
    response = render(request, 'photographygal/list_galleries.html', {'galleries': galleries})
    return response



#my picture form is getting information from the user,
# it is getting a picture uploaded by user to post and return a specif gallery by the title x
#the picture I upload will be a FK to gallery
#my picture is a primary key  to my picture list
#if valid it should take me to the specific selected gallery (pk?) usuing url and function list pictures
def add_photo(request):
    if request.method == 'GET':
        form =PictureForm()
    else:
        form=PictureForm(request.POST, files=request.FILES) #accept data from db and any files to download
        if form. is_valid():
            image = form.save(commit=False)
            print(image.gallery)
            image.save()
            return redirect (to='list_pictures', gallery_pk=image.gallery.pk)
    return render (request, "photographygal/add_photos.html", {'form':form})

def list_pictures(request, gallery_pk):
    gallery = get_object_or_404(Gallery, pk=gallery_pk)
    return render(request,'photographygal/list_pictures.html', {'gallery': gallery, 'pk':gallery_pk})#pk of of pictures to be displayed inside a gallery



def edit_gallery (request): #if registered edit and post and save or redirect to sign up
    pass

def delete_gallery (request): #if registered edit and post and save or redirect to sign up
    pass


def edit_photo (request): #if registered edit and post and save or redirect to sign up
    pass

def delete_photo (request): #if registered edit and post and save or redirect to sign up
    pass

#def upvote_star (request) jason request?

#def add or remove pic for gallery

