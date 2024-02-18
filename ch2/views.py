from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random as r

from home.models import Players


# Create your views here.
def ch2(request):
  try:
    user = Players.objects.get(id=request.COOKIES['id'])
    return render(request, f'ch2_{user.clue2}.html', {'pageno': user.clue2})
  except:
    return HttpResponse("You are not authorized to view this page")