from django .conf.urls import url
from . import views
from .views import CalendarEventLV

app_name = 'calendar'
urlpatterns = [
    url(r'^$', CalendarEventLV.as_view()),

    url(r'^(?P<pk>[0-9]+)/$', views.cal_detail, name = 'cal_detail'),
    url(r'^new/$', views.calendar_new, name='calendar_new'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.calendar_edit, name = 'calendar_edit'), ##name = 왼쪽 주소
    url(r'^calendar_search$', views.calendar_search, name = 'calendar_search'),

    ]
