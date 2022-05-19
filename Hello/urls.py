"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
     #upon visiting this link, this will send us to the urls.py in home folder
     #and then the path with "" will send us to the views.py in Home and execute the respective
     #function where we can provide the http response.
    path('about', include('Home.urls')),
    path('contact', include('Home.urls'))
]

"""
    The urls.py is just like the routes in ReactJS or node where visiting a certain link
    takes us there. Every web page that we want to render upon visiting a link has to be
    put in urlpatters under urls.py
"""
