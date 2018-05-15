# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageForm


@login_required
def images_create(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image Enregistrer avec Succes')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageForm(data=request.GET)
    context = {
        'section': 'images',
        'form': form
    }
    return redirect(request, 'images/ajouter.html', context)



# Create your views here.
