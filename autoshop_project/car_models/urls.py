from django.conf.urls import url

from . import views as model_views

urlpatterns = [
    url(r'^create$', model_views.car_model_create, name='create'),
    url(r'^$', model_views.car_model_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', model_views.car_model_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete$', model_views.car_model_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/update', model_views.car_model_update, name='update'),
]