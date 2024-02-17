from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random as r
from django.contrib import messages


# Create your views here.
pageno = -1
def ch3(request):
  global pageno
  if pageno == -1:
    pageno = r.randint(1,3)

  # post request
  if request.method == 'POST':
    messages.success(request, "Thanks for playing!")
    match pageno:
      case 1:
        name = request.POST['name']
        print(name)
        return HttpResponseRedirect('/')
      case 2:
        name = request.POST['name']
        print(name)
        return HttpResponseRedirect('/')
      case 3: 
        name = request.POST['name']
        print(name)
        return HttpResponseRedirect('/')
  
  # get request
  pageno = r.randint(1,3)
  return render(request, f'ch3_{pageno}.html', {'pageno': pageno})