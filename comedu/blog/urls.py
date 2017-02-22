from django.conf.urls import url, include
from .views import *

app_name= 'blog'
urlpatterns = [

    url(r'^$', category_LV, name='index'),
    url(r'^new/$', new_post ,name = 'new_post'),
    url(r'^not_admin/$', not_admin, name = 'not_admin'),
    url(r'^(?P<slug>[-\w]+)/$', post_LV, name='post_list'),
    url(r'^post/(?P<pk>[-\d]+)/$', post_DV, name = 'post_detail'),

    url(r'^post/(?P<pk>[-\d]+)/edit/$', post_edit, name = 'post_edit'),
    url(r'^post/(?P<pk>[-\d]+)/delete/$', post_delete, name = 'post_delete'),
    url(r'^(?P<slug>[-\w]+)/search/$', post_search, name='post_search'),




]
    # url(r'^post/(?P<pk>[-\d]+)/comments/new/$', comment_new, name='post_forms'),
