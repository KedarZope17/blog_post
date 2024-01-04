from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#create functions to show various pages

def landing_page(request):
    return render(request, 'blog/landing_page.html', {'Title': 'Welcome'})

def home(request):
    context = {
        'Posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'Title': 'About'})