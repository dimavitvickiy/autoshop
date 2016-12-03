from django.conf.urls import url

from . import views as persons_views

urlpatterns = [
    url(r'^$', persons_views.hello)
]