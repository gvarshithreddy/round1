from datetime import datetime, timezone
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random as r
from django.contrib import messages
from home.helper import *
from home.models import Players


# Create your views here.
def ch3(request):
  if request.method == 'POST':
    user = Players.objects.get(id=request.COOKIES['id'])
    if request.POST['password'] == user.password:
      messages.success(request, 'Correct Answer! You have finished the game!!')
      user.end_time = datetime.now(timezone.utc)
      user.time_taken = get_overtime_application_minutes(user.start_time, user.end_time)
      user.save()
      response = HttpResponseRedirect('/')
      response.delete_cookie('id')
      return response
    else:
      messages.error(request, 'Wrong Answer! Try Again')
      return HttpResponseRedirect('/ch3/')
  try:
    user = Players.objects.get(id=request.COOKIES['id'])
    return render(request, f'ch3_{user.clue3}.html', {'pageno': user.clue3})
  except:
    return HttpResponse("You are not authorized to view this page")