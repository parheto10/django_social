from django.conf.urls import url

from django.contrib.auth.views import (
    login,
    logout,
    logout_then_login,
)

from .views import connexion

urlpatterns = [
    #url(r'^connexion/$', connexion, name='connexion'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout_then_login/$', logout_then_login, name='logout_then_login'),
]