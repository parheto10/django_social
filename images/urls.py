from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .views import images_create

urlpatterns = [
    url(r'^ajouter/', images_create, name='images_create'),
]