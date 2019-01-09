from django.conf.urls import url
from basic_app import views

# Template Tagging
app_name = 'basic_app'


urlpatterns=[
    url(r'^other/$', views.other1, name = "other1"),
    url(r'^relative/$', views.relative, name = "relative"),
    ]
