from datetime import datetime, timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Players
import random as r

# Create your views here.

def home(request):
  if request.method == 'POST':
    rollno = request.POST['rollno']
    print(rollno)
    user = Players.objects.create(rollno=rollno,
                   start_time=datetime.now(timezone.utc),
                   clue1=r.randint(1, 3),
                    clue2=r.randint(1, 3),
                    clue3=r.randint(1, 3),
                    )
    response = HttpResponseRedirect('/ch1/')
    response.set_cookie('id', user.id)
    return response
  try:
    print('im inside try block')
    id = request.COOKIES['id']
    print(id)
    response = HttpResponseRedirect('/ch1/')
    return response
  except:
    return render(request, 'home.html', {})
  
