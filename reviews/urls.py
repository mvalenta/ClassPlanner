from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<course_id>\w+)/$', views.course_reviews, name='course_reviews'),
	url(r'^(?P<course_id>\w+)/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	)