from django.conf.urls import url
from . import views

urlpatterms = [
    url(r'^$', views.post_list, name='post_list'),
]