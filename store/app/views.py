from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(response):
    return HttpResponse("<h3>Hello World! :) :) :)</h3>")
# Testing category "about"
def about_category(response):
    return render(response, "main/html/main.html")
def man_category(response):
    return render(response, "main/html/man.html")
def small_kids_category(response):
    return render(response, "main/html/small kids.html")
def women_category(response):
    return render(response, "main/html/women.html")
