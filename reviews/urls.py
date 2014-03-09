from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<review_id>\d+)/$', views.detail, name='detail'), # move this to be /<course_id>/<review_id>
	url(r'^(?P<course_id>\w+)/$', views.course_reviews, name='course_reviews'),
	)