from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random as r


# Create your views here.
pageno = -1
def ch1(request):
  global pageno
  if pageno == -1:
    pageno = r.randint(1,3)

  # post request
  if request.method == 'POST':
        match pageno:
          case 1:
            name = request.POST['name']
            print(name)
            return HttpResponseRedirect('/ch2/')
          case 2:
            name = request.POST['name']
            print(name)
            return HttpResponseRedirect('/ch2/')
          case 3: 
            name = request.POST['name']
            print(name)
            return HttpResponseRedirect('/ch2/')
  
  # get request
  pageno = r.randint(1,3)
  return render(request, f'ch1_{pageno}.html', {'pageno': pageno})