from django .conf.urls import url
from . import views
from .views import CalendarEventLV

<<<<<<< HEAD
app_name = 'calendar'
=======
app_name = 'comedu_calendar'
>>>>>>> fffc4bed065a49a01fedf926fb34de3072df74dd
urlpatterns = [
    url(r'^$', CalendarEventLV.as_view()),

    url(r'^(?P<pk>[0-9]+)/$', views.cal_detail, name = 'cal_detail'),
    url(r'^new/$', views.calendar_new, name='calendar_new'),
<<<<<<< HEAD
    url(r'^(?P<pk>[0-9]+)/edit$', views.calendar_edit, name = 'calendar_edit'), ##name = 왼쪽 주소
    url(r'^calendar_search$', views.calendar_search, name = 'calendar_search'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.calendar_delete, name = 'calendar_delete'),
    ]
=======
    url(r'^(?P<pk>[0-9]+)/edit$', views.calendar_edit), ##url지정 어떻게 해줘야 되냐.....

]
>>>>>>> fffc4bed065a49a01fedf926fb34de3072df74dd
