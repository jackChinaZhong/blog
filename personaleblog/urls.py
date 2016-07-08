from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^index/',index,name='index'),
    url(r'^category/(?P<categroy_name>[^/]+)/$',category,name='category'),
    url(r'^article/(?P<article_id>[^/]+)/$',detail,name='article'),
]