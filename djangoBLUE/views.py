from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hello im mohammad')
  return render(request , 'about.html')

def home(request):
    #return HttpResponse('home')
  return render (request , 'Home.html')