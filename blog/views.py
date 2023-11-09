from django.shortcuts import render
from django.http import HttpResponse

#create functions to show various pages
posts = [
    {
        'Author' : 'Kedar Zope',
        'Title' : 'Life as an AI worker specialist',
        'Content' : 'Work-life balance is little unbalanced,\
            but the area of work is wide. This enables me to get\
            into more technologies and understand better\
            client-handling at the same time.',
        'Date_posted': 'Nov 01, 2023'
    },
    {
        'Author' : 'Mayuresh K',
        'Title' : 'Life as an AI worker specialist',
        'Content' : 'My work of area is little different compared\
            to the other team mates. I am more involved into the backend',
        'Date_posted': 'Nov 01, 2023'
    },
        {
        'Author' : 'Abhishek Tripathi',
        'Title' : 'Life as an customer relationship manager',
        'Content' : 'It is crucial to have a good customer support.\
            I need to analyse the situation, and look for a solution\
            to team members and handle the client simultaneouly. The\
            time plays very critical role here and sometimes the pressure\
            is tough deal.'
    }
]

def home(request):
    context = {
        'Posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
