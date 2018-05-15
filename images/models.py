# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Images(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'images_cree')
    titre = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    description = models.TextField(blank=True)
    ajouter = models.DateTimeField(auto_now_add=True, db_index=True)

    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_like', blank=True)

    def __unicode__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Images, self).save(*args, **kwargs)






# Create your models here.
