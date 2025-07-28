from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

def home(request):
    #body
    return HttpResponse('<h1>Welcome to my weblog ....<h1>')

def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'posts/posts_list.html', context=context)