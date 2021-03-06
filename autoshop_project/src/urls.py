"""autoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from persons.views import (login_view, logout_view)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^engines/', include('engines.urls', namespace='engines')),
    url(r'^models/', include('car_models.urls', namespace='car_models')),
    url(r'^cars/', include('cars.urls', namespace='cars')),
    url(r'^equipments/', include('equipments.urls', namespace='equipments')),
    url(r'^contracts/', include('contracts.urls', namespace='contracts')),
    url(r'^factories/', include('factories.urls', namespace='factories')),
    url(r'^', include('autoshops.urls', namespace='autoshops')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)