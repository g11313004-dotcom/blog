from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Post

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())

def showPost(request,id):
    try:
        post = Post.objects.get(id = id)
        if post !=None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

