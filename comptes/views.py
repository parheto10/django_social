# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def connexion(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
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
        login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    return render(request, 'comptes/login.html', context)


# Create your views here.
