from django.conf.urls import url

from . import views as autoshop_views

urlpatterns = [
    url(r'^$', autoshop_views.autoshop_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', autoshop_views.autoshop_detail, name='detail'),
]