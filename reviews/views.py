from django.shortcuts import render
from django.http import HttpResponse

from reviews.models import Course, Review

# Create your views here.

def index(request):
	course_list = Course.objects.all()
	context = { 'course_list': course_list	}
	return render(request, 'reviews/index.html', context)

def review_detail(request, course_id, review_id):
	return HttpResponse("You're looking at review %s for %s" % (review_id, course_id))

def course_reviews(request, course_id):
	review_list = Review.objects.filter(course=course_id)
	context = { 'course_id': course_id, 'review_list': review_list }
	return render(request, 'reviews/course_reviews.html', context)