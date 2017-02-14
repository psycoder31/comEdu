from django .conf.urls import url
from . import views
from .views import CalendarEventLV

app_name = 'calendar'

urlpatterns = [
    url(r'^$', CalendarEventLV.as_view()),

    url(r'^(?P<pk>[0-9]+)/$', views.cal_detail, name = 'cal_detail'),

    url(r'^new/$', views.calendar_new, name='calendar_new'),

    url(r'^(?P<pk>[0-9]+)/edit$', views.calendar_edit, name = 'calendar_edit'),
     ##name = 왼쪽 주소

    url(r'^(?P<pk>[0-9]+)/delete$', views.calendar_delete, name = 'calendar_delete'),

    url(r'^search/$', views.calendar_search, name = 'calendar_search'),

    url(r'^success_popup/$', views.calendar_success_popup, name = 'calendar_success_popup'),

    ]
