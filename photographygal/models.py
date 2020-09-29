from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from users.models import User
#from django.core.exceptions import FieldDoesNotExist, FieldError
#from imagekit___

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










# Create your models here.
class Gallery (models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE, related_name='galleries', null=True, blank=True) #one user may create many galleries
    title = models.CharField (max_length = 150, null=False, blank=False)
    description = models.TextField(max_length= 400)
    image = models.ImageField(upload_to='gallery', null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit (200, 200)],format='JPEG',options={'quality': 80})

    def __str__(self):
        return self.title




class Picture (models.Model):
    gallery = models.ForeignKey(to=Gallery, on_delete = models.CASCADE, related_name='pictures', null=True, blank=True) # gallery FK to picture
    title = models.CharField(max_length = 150, null=False, blank=False)
    description = models.TextField(max_length= 400, null=False, blank=False)
    image = models.ImageField(upload_to='gallery', null=True) #inside media dir gallery (?)

