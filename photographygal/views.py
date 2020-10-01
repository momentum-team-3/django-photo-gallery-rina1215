from django.shortcuts import render, redirect, get_object_or_404
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from django.views import View
from .models import Gallery, Picture, Comments
from .forms import  GalleryForm, PictureForm, CommentsForm


def homepage(request):
    return render(request, "photographygal/homepage.html")


def add_gallery(request):
    if request.method == 'GET':
        form =GalleryForm()
    else:
        form=GalleryForm(data=request.POST, files=request.FILES) 
        if form. is_valid():
            form.save()
            return redirect (to='list_gallery')
    return render (request, "photographygal/add_galleries.html", {'form':form})


def list_gallery (request):
    galleries = Gallery.objects.all()
    response = render(request, 'photographygal/list_galleries.html', {'galleries': galleries})
    return response


#the picture I upload will be a FK to gallery
#my picture is a primary key  to my picture list
#if valid it should take me to the specific selected gallery (pk?) usuing url and function list pictures
def add_photo(request):
    if request.method == 'GET':
        form =PictureForm()
    else:
        form=PictureForm(request.POST, files=request.FILES)
        if form. is_valid():
            image = form.save(commit=False)
            print(image.gallery)
            image.save()
            return redirect (to='list_pictures', gallery_pk=image.gallery.pk)
    return render (request, "photographygal/add_photos.html", {'form':form})


def add_comment(request, image_pk):
    image = get_object_or_404(Picture, pk = image_pk)
    if request.method == 'GET':
        form =CommentsForm()
    else:
        form=CommentsForm(data = request.POST)
        if form. is_valid():
            comments = form.save(commit=False)
            comments.author = request.user
            comments.image = image
            comments.save()
            return redirect (to='list_pictures', gallery_pk=image.gallery.pk)
    return render (request, "photographygal/add_comment.html", {'form':form, 'image':image})

def list_pictures(request, gallery_pk):
    gallery = get_object_or_404(Gallery, pk=gallery_pk)
    return render(request,'photographygal/list_pictures.html', {'gallery': gallery, 'pk':gallery_pk})#pk of of pictures to be displayed inside a gallery



def edit_gallery (request): 
    pass

def delete_gallery (request, gallery_pk): #
    gallery = get_object_or_404(Gallery, pk=gallery_pk)
    if request.method == 'POST':
        gallery.delete()
        return redirect(to = "homepage")
    return render(request,"photographygal/delete_gallery.html", {'gallery': gallery, 'pk':gallery_pk})



def edit_photo (request): #if registered edit and post and save or redirect to sign up
    pass

def delete_photo (request): #if registered edit and post and save or redirect to sign up
    pass

#def upvote_star (request) jason request?
