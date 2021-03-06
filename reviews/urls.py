from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('',
	url(r'^/$', views.index, name='index'),
	url(r'^/create$', views.create_review, name='create_review'),
	url(r'^/(?P<course_id>\w+)/create$', views.create_review_for, name='create_review_for'),
	url(r'^/(?P<course_id>\w+)$', views.course_reviews, name='course_reviews'),
	#url(r'^(?P<course_id>\w+)/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	)