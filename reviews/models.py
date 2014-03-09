from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
	coursename 	= models.CharField(max_length=15, primary_key=True)

	def __str__(self):
		return self.coursename

# Create your models here.
class Review (models.Model):
	course 		= models.ForeignKey(Course)
	author 		= models.CharField(max_length=50)
	professor 	= models.CharField(max_length=50)
	publishdate = models.DateField(auto_now_add=True)
	score 		= models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
	text 		= models.TextField()

	def __str__(self):
		return "Review of %s by %s: %d/5" % (course, author, score)