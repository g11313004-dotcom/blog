from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from home.models import Post

def homepage(request):
    posts = Post.objects.all()
    lists = list()
    for index,post in enumerate(posts,start=1):
        s = "<p>"
        s+= f"No.{index:02d}:" + str(post) + "<hr>"
        s+= post.body + "</p>"
        lists.append(s)
    return HttpResponse(lists)    
