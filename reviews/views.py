import sys
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from reviews.models import Course, Review, ReviewForm

# Create your views here.

def index(request):
	course_list = Course.objects.all()
	context = { 'course_list': course_list	}
	return render(request, 'reviews/index.html', context)


def course_reviews(request, course_id):
	review_list = Review.objects.filter(course=course_id)
	count = len(review_list)
	if count < 1:
		return render(request, 'reviews/course_reviews.html', { 'course_id': course_id })
	else:
		total = sum(r.score for r in review_list)
		average = total / count
		context = { 'course_id': course_id, 'review_list': review_list , 'average_rating': average}
		return render(request, 'reviews/course_reviews.html', context)


def create_review(request):
	if(request.method == 'POST'):
		print "Received POST"
		try:
			rating = request.POST['rating']
			course = request.POST['course']
			author = request.POST['author']
			professor = request.POST['professor']
			rating = int(request.POST['rating'])
			text = request.POST['text']

			if rating >= 1 and rating <= 5:
				courseobj = None

				try:
					courseobj = Course.objects.get(coursename=course)
				except Course.DoesNotExist:
					courseobj = Course(coursename=course)
					courseobj.save()

				r = Review(course=courseobj, author=author, professor=professor, score=rating, text=text)
				r.save()

				print "Saved %s" % r

				return HttpResponseRedirect(reverse('course_reviews', args=(course,)))
			else:
				raise ValueError()
		except:
			context = { 'error_message': "Please fill all fields",
						'course': 	 course,
						'author': 	 author,
						'professor': professor,
						'rating': 	 rating,
						'text': 	 text }
			return render(request, 'reviews/create_review.html', context)
	else:
		return render(request, 'reviews/create_review.html', None)