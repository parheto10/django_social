# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import unicode_literals

import os
import time

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import get_thumbnail

def upload_image(self, filename):
    real_name, extension = os.path.splitext(filename)
    name = str(int(time.time())) + extension
    return "profile/images/" + self.user.username + "." + extension

class Profile(models.Model):
    CIVILITY_CHOICES = (
        ('Mr.', 'Mr.'),
        ('MME', 'Mme')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    sexe = models.CharField(max_length=3, choices=CIVILITY_CHOICES, default='M.', verbose_name="Civilité")
    date_naiss = models.DateField(verbose_name="Date de naissance", blank=True, null=True)
    pays = CountryField(max_length=255)
    ville = models.CharField(max_length=255)
    contact = PhoneNumberField()
    image = models.ImageField(upload_to='images_profiles', blank=True)
    emploie = models.BooleanField(default=False, verbose_name="Disponible pour Emploie ?")
    facebook = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def thumb(self):
        if self.image:
            thumb = get_thumbnail(self.image, "50x50", crop='center', quality=100)
            return "<image src='%s' />" % thumb.url
        else:
            return "Aucun photo"

    thumb.short_description = ('Image')
    thumb.allow_tags = True



# Create your models here.
