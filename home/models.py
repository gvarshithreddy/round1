from django.db import models
# from helper import get_overtime_application_minutes
# Create your models here.

class Players(models.Model):
  rollno = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField(null=True, blank=True)
  clue1 = models.IntegerField()
  clue2 = models.IntegerField()
  clue3 = models.IntegerField()
  password = models.CharField(max_length=100, default="password")
  time_taken = models.FloatField(null=True, blank=True)

class question_answers(models.Model):
  clue = models.IntegerField()
  question = models.CharField(max_length=100)
  answer = models.CharField(max_length=100)