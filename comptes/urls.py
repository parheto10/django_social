from django.conf.urls import url, include

from django.contrib.auth.views import (
    login,
    logout,
    logout_then_login,
    password_change,
    password_change_done,

    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

from .views import connexion, dashboard, register, edit

urlpatterns = [
    #url(r'^connexion/$', connexion, name='connexion'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^register/$', register, name='register'),
    url(r'^edit/$', edit, name='edit'),
    #Connexion et Deconnexion
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout_then_login/$', logout_then_login, name='logout_then_login'),

    #Modifier Mot e Passe
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
    url(r'^password-reset/$', password_reset, name="password_reset"),
    url(r'^password-reset/done/$', password_reset_done, name="password_reset_done"),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),
    url(r'^password-reset/complete/$',password_reset_complete, name="password_reset_complete"),
]