from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Players

# Create your views here.

def home(request):
  if request.method == 'POST':
    username = request.POST['username']
    user = Players.objects.create(name=username,
                   start_time=datetime.now())
    return HttpResponseRedirect('/ch1/')
  return render(request, 'home.html', {})
