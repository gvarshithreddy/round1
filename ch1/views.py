from django.shortcuts import render
import random as r

# Create your views here.

def ch1(request):
  pagegno = r.randint(1,3)
  match pagegno:
    case 1:

      return render(request, '1.html', {'hero': 'Superman'})
    case 2:
      return render(request, '2.html', {})
    
    case 3:
      return render(request, '3.html', {})