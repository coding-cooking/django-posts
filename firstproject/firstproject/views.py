#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello world. This is home.")
    return render(request, 'home.html')

def aboutpage(request):
    # return HttpResponse("Hello world. This is about page.")
    return render(request, 'about.html')