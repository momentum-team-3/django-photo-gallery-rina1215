"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from api import views as api_views


#from view of my app to bring my function 
from photographygal import views

router = routers.DefaultRouter()
router.register('pictures', api_views.PictureViewSet)
router.register('galleries', api_views.GalleryViewSet) #equivalent to path, related to classpicture viewset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),



    #GALLERY url's path
    path('photographygal/add_gallery/', views.add_gallery, name='add_gallery'),
    path('photographygal/list_gallery/', views.list_gallery, name="list_gallery"),
    #path('photographygal/delete_gallery/<int:gallery_pk>', views.delete_gallery, name="delete_gallery"),
    path('gallery/delete_gallery/<int:gallery_pk>/', views.delete_gallery, name='delete_gallery'),

    #PHOTO url's path
    path('photographygal/add_photo/', views.add_photo, name='add_photo'),
    path('photographygal/list_pictures/<int:gallery_pk>/', views.list_pictures, name='list_pictures'), #pk picture to an specific gal 


     #API url's path
    path('api/', include(router.urls)),
    path('api/gallery/', api_views.GalleryListView.as_view()),
    path('api/gallery/<int:gallery_pk>/', api_views.GalleryDetailView.as_view()),
    path('api/gallery/<int:pk>/images/', api_views.GalleryImageView.as_view()),
    #path('api/pictures', api_views.)


]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns