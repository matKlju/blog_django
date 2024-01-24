from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Mati',
        'title': 'post 1',
        'content': 'First content',
        'date_posted': 'August 2018'
    },
     {
        'author': 'Jane',
        'title': 'post 2',
        'content': 'Second content',
        'date_posted': 'August 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



