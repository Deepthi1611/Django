"""
URL configuration for DjangoSample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('app1/', include('app1.urls')),
    path("__reload__/", include("django_browser_reload.urls")) 
    # path to browser reload
    # this path should always be the last path because this is a heavy path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# the above line is essential for serving media files when developing your Django application locally. 
# It makes sure that user-uploaded files can be accessed via URLs that start with MEDIA_URL, 
# and Django knows where to find those files on the file system (MEDIA_ROOT).
