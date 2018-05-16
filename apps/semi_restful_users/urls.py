
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^/new$',views.addUser),
    url(r'^/delete/(?P<id>\d+)$',views.distroy),
    url(r'^/show/(?P<id>\d+)$',views.show),
    url(r'^/edit/(?P<id>\d+)$',views.edit),
]