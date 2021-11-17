from django.shortcuts import render

from apps.blog.models import Post


def listview_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/list_post.html', {'posts': posts})

