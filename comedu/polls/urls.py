from django.conf.urls import url, include

from .views import poll_new

urlpatterns = [
    url(r'new/$', poll_new, name='new-poll')
]
