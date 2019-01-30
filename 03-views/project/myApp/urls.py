from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^attribute/$', views.attribute),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^showregister/$', views.showregister),
    url(r'^showregister/register/$', views.register),
    url(r'^showresponse/$', views.showresponse),
    url(r'^cookietest/$', views.cookietest),
    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),


    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$', views.showmain),
    url(r'^quit/$', views.quit),

    

]
