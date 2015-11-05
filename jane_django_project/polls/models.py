from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=40)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    emailId = models.EmailField()
    phoneNumber = models.IntegerField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text

    def was_published_in_last_week(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

    was_published_in_last_week.admin_order_field = 'pub_date'
    was_published_in_last_week.boolean = True
    was_published_in_last_week.short_description = 'Published this week?'

class Choice(models.Model):	
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.choice_text

class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
