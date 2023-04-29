# from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
   
def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def user(request, name):
    return HttpResponse(f"<h2>Имя: {name}</h2>")