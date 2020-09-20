from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
#from users.models import User
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
    #owner = models.ForeignKey(User, on delete=model.CASCADE, related_name='gallery') #if an owner is deleted all its pictures gets deleted
    #featured_photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name= '+',  null=True, blank=True)
    #cover_photo=models.ForeignKey('Picture', on_on delete=models.CASCADE, related_name=....)#this is the default thumbnail
    #cover_photo is public BooleanField?
    #photo_thumbnail can be an image field . the relationship is one gallery can have one thumbnail from default photo. ThumbNail is FK to gallery
    title = models.CharField (max_length = 250)
    date_added = models.DateField(auto_now_add=True, null=True)
    date_updated = models.DateField(auto_now=True, null=True)
    comments = models.TextField(max_length= 400)
    #public_gallery = models.BooleanField(default=True)




class Picture (models.Model):
    #creator = models.ForeignKey(User, on delete = model.CASCADE, related_name='pictures') if an owner is deleted all its pictures gets deleted
    title = models.CharField(max_length = 150)
    #picture_thumb = ImageSpecField(source="picture", processors=[ResizeToFit(200,200)], format="JPEG", options={"quality": 80})
    comments = models.TextField(max_length= 400)
    #gallery = models.ForeignKey (Gallery, on_delete = models.CASCADE) #Many to one ---> many pictures to one album
    #uploaded time, datefield
    #modified by date field
    #upvoted = models.ManyToManyField(User, related_name='favorite_photos', blank=True) any registered user my upvote many pictures #should I use json


#class Profile(models.Model):
    #avatar = models.ImageField(upload_to='avatars')
    #gallery_thumbnail = ImageSpecField(source='gallery',
                                    #processors=[ResizeToFill(100, 50)],
                                    #format='JPEG',
                                    #options={'quality': 60})

#profile = Profile.objects.all()[0]
#print(profile.gallery_thumbnail.url)    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
#print(profile.gallery_thumbnail.width)  # > 100