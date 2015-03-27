from django.conf.urls import patterns, url

from Login import views

urlpatterns = patterns('',
	url(r'Register/$', views.register, name='register'),
	url(r'^$', views.index, name='index'),
	)
