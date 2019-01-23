from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^students/$', views.students),
    url(r'^students2/$', views.students2),
    url(r'^stu/(\d+)/$', views.stupage),
    url(r'^studentsearch/$', views.studentsearch),



    url(r'^addstudents/$', views.addstudents),
    url(r'^addstudents2/$', views.addstudents2),
]
