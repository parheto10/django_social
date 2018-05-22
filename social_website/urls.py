"""social_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('django.contrib.auth.urls')),
    url(r'^comptes/', include('comptes.urls', app_name="comptes", namespace="comptes")),
    url(r'^images/', include('images.urls', app_name="images", namespace="images")),
    #url('social-auth/', include('social.apps.django_app.urls', namespace="social")),
    url(r'social-auth/', include('social_django.urls', namespace='social')),
    url(r'', home, name='home'),
]

urlpatterns += [
    url(r'^captcha/', include('captcha.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)