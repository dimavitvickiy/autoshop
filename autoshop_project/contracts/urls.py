from django.conf.urls import url

from . import views as contract_views

urlpatterns = [
    url(r'^$', contract_views.contract_list, name='list'),
    url(r'^(?P<id>\d+)/$', contract_views.contract_detail, name='detail'),
]