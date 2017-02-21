from django .conf.urls import url
from . import views
from .views import CalendarEventLV

app_name = 'calendar'

urlpatterns = [
    url(r'^$',views.calendar_show),

    url(r'^(?P<pk>[0-9]+)/$', views.cal_detail, name = 'cal_detail'),

    url(r'^new/$', views.calendar_new, name='calendar_new'),

    url(r'^(?P<pk>[0-9]+)/edit$', views.calendar_edit, name = 'calendar_edit'),

    url(r'^(?P<pk>[0-9]+)/delete/$', views.calendar_delete, name = 'calendar_delete'),##뒤에 answer때문에 /생겨서 주소에도 마지막에 /넣어줘야됨

    url(r'^search/$', views.calendar_search, name = 'calendar_search'),

    url(r'^success_popup/$', views.calendar_success_popup, name = 'calendar_success_popup'),

    url(r'^(?P<pk>[0-9]+)/delete_popup$', views.calendar_delete_popup, name = 'calendar_delete_popup'),

    url(r'^show$',  CalendarEventLV.as_view(), name = 'calendar_show'),

    ]
