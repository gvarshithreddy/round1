from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random as r
from home.models import *


# Create your views here.


def ch1(request):
  try:
    user = Players.objects.get(id=request.COOKIES['id'])
    return render(request, f'ch1_{user.clue1}.html', {'pageno': user.clue1})
  except:
    return HttpResponse("You are not authorized to view this page")