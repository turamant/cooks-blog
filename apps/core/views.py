from django.http import HttpResponse
from django.shortcuts import render

from apps.blog.models import Post, Comment


def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    comments = Comment.objects.all()
    return render(request, 'core/frontpage.html', {'posts': posts, 'comments': comments})

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

