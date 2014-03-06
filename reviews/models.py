from django.db import models

class Course(models.Model):
	coursename 	= CharField(max_length=15, primary_key=True)

	def __str__(self):
		return self.coursename

# Create your models here.
class Review (models.Model):
	course 		= models.ForeignKey(models.Course)
	author 		= CharField(max_length=50)
	professor 	= CharField(max_length=50)
	publishdate = DateField(auto_now_add=True)
	score 		= IntegerField(validators=[MaxValueIndicator(5), MinValueIndicator(1)])
	text 		= TextField()

	def __str__(self):
		return "Review of %s by %s: %d/5" % (course, author, score)