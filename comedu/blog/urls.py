from django.conf.urls import url, include
from .views import *

app_name= 'blog'
urlpatterns = [

    url(r'^$', category_LV, name='index'),

    url(r'^new/$', new_post ,name = 'new_post'),

    url(r'^newalbum/$', new_album ,name = 'new_album'),

    url(r'^album/$', album_LV, name = 'album_list'),

    url(r'^not_admin/$', not_admin, name = 'not_admin'),

    url(r'^album/search/$', album_search, name='album_search'),

    url(r'^(?P<slug>[-\w]+)/$', post_LV, name='post_list'),

    url(r'^post/(?P<pk>[-\d]+)/$', post_DV, name = 'post_detail'),

    url(r'^post/(?P<pk>[-\d]+)/edit/$', post_edit, name = 'post_edit'),

    url(r'^post/(?P<pk>[-\d]+)/delete/$', post_delete, name = 'post_delete'),

    url(r'^(?P<slug>[-\w]+)/search/$', post_search, name='post_search'),

    url(r'^album/(?P<pk>[-\d]+)/$', album_DV, name = 'album_detail'),

    url(r'^album/(?P<pk>[-\d]+)/edit/$', album_edit, name = 'album_edit'),

    url(r'^album/(?P<pk>[-\d]+)/delete/$', album_delete, name = 'album_delete'),

    # url(r'^album/(?P<pk>[-\d]+)/commentedit/$', album_commentedit, name = 'album_commentedit'),



]
