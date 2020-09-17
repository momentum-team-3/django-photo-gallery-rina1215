
from django.shortcuts import render, redirect


#GALLERY
#All Gallery thumbnail can be viewed by all---public
#Ea gallery can be selected to be viewed by reg users
#Ea gallery holds many pictures- one to many--> many to many field
#Galleries should have thumbnails and default photos
#Gallery thumbnail should be the default photo chosen the owner
#Reg usuers can open and view all pic from ea gallery and upvote
#Gallery owner can select default picture from its own photo gallery
#Gallery can be edited and deleted by its owner
#Owner is PK to gallery
#Gallery is PK to photo in gallery
#Has tittle, owner, thumbnail, default picture
#Gallery can be deleted, added by PK
#created, updated time field
#only registered owner can create and add pictures to a gallery


#PICTURES
#Can be upvoted by al reg users
#Can be viewed by all reg users
#One picture is be selected by its owner to be the default pic of gallery
#Ea picture can be commented by any reg user --
#Ea picture can have comments by reg users --many to many field
#A default picture must be displayed as thumbnail of a gallery  ------->>>should I have a thumbnail class?
#Ea pic would be listed to display when thumbnail Gal is selected
#Ea pic may be added or deleted by its owner ---->owner is PK to each pic
######Has tittle, comment field, an ability to be upvoted, deleted, added to gallery, viewed and edit/update
######created, updated time field
#upvoted pictures can be displayed-listed


#Users
#Can be registered user, can be public users, can be an registered owner of a gallery and pics
#_____________________________________________________________
#public users can view all gallery thumbnails and title of it
#public has option to sign up to be registered
#_____________________________________________________________
#Owner can select a picture to a default gallery thumbnail
#Owner can create gallery, upload pictures, delete pictures from Gallery, delete gallery, add comments to picture
#___________________________________________________________
#Reg user can view all galleries, all pictures, all comments attached to ea pic but can't edit 
#Reg user can search any pic by tittle
#Reg user can upvote any picture from any gallery
#Reg user can view list of upvoted pictures
#Reg users can be the creator its own galleries, add, delete, view,update
# Create your views here.


#get and post for returning responses
#my urls will be routed to ea functions
#what can I user do when on it home page?
#What can I user request?

#sign up
#return home
#view list of all default thumbnails assigned to ea gallery (public)
#view deatails of gallery if resgistered, if not redirect to sign up page
#add a gallery if registered if not redirect sign up page
#add pictures to gallery if signed up
#view_all pictures added to gallery as a list
#detail_pictures------view individual pictures w comments
#delete_gallery
#delete_photo
#list_all upvoted or stared
##search by titles (or use comments as part of search db search)



#CRUD


def homepage(request):
    return render(request, "photographygal/homepage.html")
    # home page to list all gallery thumnails so maybe its list_gallery.html


def list_pictures(request): #when requesting an url of individual gallery
    pass

def show_pic_details (request): #if registered
    pass

def upvote_star (request): #option to registered users
    pass 

def show_gallery (request): #home listed all gallery thumbnail default pic redirect to list.html
    pass

def add_photo (request): #add to gallery by registered user
    pass

def add_gallery(request): #if reg or else redirect to sign up
    pass

def edit_gallery (request): #if registered edit and post and save or redirect to sign up
    pass

#def upvote_star (request) jason request?

#def add or remove pic for gallery