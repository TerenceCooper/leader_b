from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$/', views.leader_board),
	url(r'^leader_board/$', views.leader_board, name='leader_board')
]
