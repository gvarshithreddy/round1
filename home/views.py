from datetime import datetime
from django.shortcuts import render
from .models import Players

# Create your views here.

def home(request):
  if request.method == 'POST':
    username = request.POST['username']
    user = Players.objects.create(name=username,
                   start_time=datetime.now())
    return render(request, 'home.html', {'username': username})
  return render(request, 'home.html', {})
