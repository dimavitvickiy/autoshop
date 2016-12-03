from django.conf.urls import url

from . import views as factory_views

urlpatterns = [
    url(r'^create$', factory_views.factory_create, name='create'),
    url(r'^$', factory_views.factory_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', factory_views.factory_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete$', factory_views.factory_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/update', factory_views.factory_update, name='update'),
]