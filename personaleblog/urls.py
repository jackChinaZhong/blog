from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^index/',index,name='index'),
    url(r'^category/(?P<category_name>[^/]+)/$',category,name='category'),
    url(r'^article/(?P<article_id>[^/]+)/$',detail,name='article'),
    url(r'^tag/(?P<tag_name>[^/]+)/$',detail,name='tag'),
    url(r'^login/$',loginsafe,name='login'),
    url(r'^logout/$',logoutsafe,name='logout'),
    url(r'^register/$',register,name='register'),
]