from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("<h1>This Is Home Page</h1>")


def contact(request):
    return HttpResponse("<h1>This Is Contact Page </h1>")


def about(request):
    return HttpResponse("<h1>About Us </h1>")
