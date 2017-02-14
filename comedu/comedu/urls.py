"""comedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

# from comedu_calendar.views import *
from customuser.views import mainView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, name='login',kwargs={
        'template_name': 'login.html'
        }),
    url(r'^logout/', auth_views.logout, name='logout'),

    ##add for calendar
    url(r'^calendar/', include('comedu_calendar.urls', namespace = 'calendar')),
    # url(r'^search/$', calendar_search),

    url(r'^blog/', include('blog.urls')),


    # polls app url
    url(r'^polls/', include('polls.urls')),

    # main page
    url(r'^$', mainView, name='home'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
