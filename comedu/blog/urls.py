from django .conf.urls import url, include
from .views import *

app_name= 'blog'
urlpatterns = [

    url(r'^$', PostLV.as_view(), name='index'),

    url(r'^post/$', PostLV.as_view(), name='post_list'),

    url(r'^post/(?P<pk>[-\d]+)/$', PostDV.as_view(), name = 'post_detail'),

    url(r'^post/(?P<pk>[-\d]+)/comments/new/$', comment_new, name='post_forms'),

    #1 url(r'visit^$', PostLV.as_view(), name='index'),

    #url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    ##url(r'^'(?P<year>\d{4})/$', PostYAV.as_view(), name =   )

    ##url(r'^')

    ##url(r'^')

    ##url(r'^')

]
