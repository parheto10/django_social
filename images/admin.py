# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Images

class ImageAdmin(admin.ModelAdmin):
    list_display = ['titre', 'slug', 'image', 'ajouter']
    list_filter = ['ajouter']

admin.site.register(Images, ImageAdmin)




# Register your models here.
