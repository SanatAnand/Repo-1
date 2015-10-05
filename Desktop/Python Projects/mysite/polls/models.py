import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def  was_published_recently(self):
		return self.pub_date >=timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(Question)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class Student(models.Model):
	roll_no=models.CharField(validators=[RegexValidator(regex='^.{9}$', message='Length has to be 9', code='nomatch')], max_length=9) #Can be improved by allowing only valod roll numbers
	name=models.CharField(max_length=50)
