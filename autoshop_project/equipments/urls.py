from django.conf.urls import url

from . import views as equipment_views

urlpatterns = [
    url(r'^create$', equipment_views.equipment_create, name='create'),
    url(r'^$', equipment_views.equipment_list, name='list'),
    url(r'^(?P<id>\d+)/$', equipment_views.equipment_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete$', equipment_views.equipment_delete, name='delete'),
    url(r'^(?P<id>\d+)/update', equipment_views.equipment_update, name='update'),
]