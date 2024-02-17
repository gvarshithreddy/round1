from django.db import models
# from helper import get_overtime_application_minutes
# Create your models here.

class Players(models.Model):
  name = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField(null=True, blank=True)
  time_taken = models.FloatField(null=True, blank=True)