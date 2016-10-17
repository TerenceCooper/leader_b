from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.list),
	url(r'^list/$', views.list, name='files.list')
]
