from django.conf.urls import url

from . import views as car_views

urlpatterns = [
    url(r'^create$', car_views.car_create, name='create'),
    url(r'^(?P<id>\d+)/$', car_views.car_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete$', car_views.car_delete, name='delete'),
    url(r'^(?P<id>\d+)/update', car_views.car_update, name='update'),
]