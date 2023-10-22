from django.shortcuts import render
from django.http import HttpResponse
#create functions to show various pages

def home(request):
    return HttpResponse("Blog Home")

def about(request):
    return HttpResponse("Information about blog page")
