from django.conf.urls import url

from . import views as engine_views

urlpatterns = [
    url(r'^create$', engine_views.engine_create, name='create'),
    url(r'^$', engine_views.engines_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', engine_views.engine_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete$', engine_views.engine_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/update', engine_views.engine_update, name='update'),
]