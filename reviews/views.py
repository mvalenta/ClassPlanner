from django.shortcuts import render
from django.http import HttpResponse

from reviews.models import Course, Review

# Create your views here.

def index(request):
	course_list = Course.objects.all()
	context = { 'course_list': course_list	}
	return render(request, 'reviews/index.html', context)

def detail(request, review_id):
	return HttpResponse("You're looking at review %s" % review_id)

def course_reviews(request, course_id):
	return HttpResponse("You're looking at reviews of %s" % course_id)