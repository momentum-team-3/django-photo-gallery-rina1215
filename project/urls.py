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
#from django.conf.urls.static import static

#from view of my app to bring my function 
from photographygal import views



#list of with individual routes to match with view function to get executed

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

    path('photographygal/add_gallery/', views.add_gallery, name='add_gallery'),
    #path('photographygal/add_photos/', views.add_photo, name='add_photo'),

    #gallery view url
    #path("gallery/view/<int:gallery_pk>", views.view_gallery, name="view_gallery"),
    #path('photographygal/', views.list_gallery, name='gallery'),
    #path('photographygal/', views.add_gallery, name='gallery'),
    #"/photographygal/add_galleries.html"

]#+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns