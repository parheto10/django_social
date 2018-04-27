# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import message
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .forms import LoginForm, InscriptionForm, ProfileEdit, UserEditForm
from .models import Profile

def connexion(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Bienvenu")
                else:
                    return HttpResponse("Compte Desactive")
            else:
                return HttpResponse("Parametres de Connexion Invalides!!")
    else:
        form = LoginForm()
    context = {
        'form':form
    }
    return render(request, 'comptes/login.html', context)

def register(request):
    if request.method == 'POST':
        user_form = InscriptionForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])

            new_user.save()
            profile = Profile.objects.create(user=new_user)
            context = {
                'new_user' : new_user,
            }
            return render(request, 'comptes/welcome.html', context)
    else:
        user_form = InscriptionForm()
    context = {
        'user_form': user_form
    }
    return render(request, 'comptes/register.html', context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEdit(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Modifier avec Succes')
        else:
            messages.error(request, 'Desole Une Erreur est Survenu lors de la Modification!!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEdit(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'comptes/edit.html', context)



@login_required
def dashboard(request):
    context = {
        'section': 'dashboard',
    }
    return render(request, 'comptes/dashboard.html', context)
# Create your views here.
