"""
URL configuration for bloggingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views  #views inside bloggingSystem
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as blogView  #views inside blogs app, name cannot be same 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('<slug:blog_slug>/', blogView.blogs, name='blogs'),
    path('blogs/search/', blogView.search, name="search"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

"""+static(settings.MEDIA_URL, document_root = MEDIA_ROOT) 
with the help of this we can access the uploaded files 
otherwise django doesn't serve the uploaded files
for this also:
        from django.conf.urls.static import static
        from django.conf import settings
"""