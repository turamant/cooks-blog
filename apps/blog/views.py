from django.shortcuts import render, get_object_or_404

from apps.blog.forms import CommentForm
from apps.blog.models import Post


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'form': form})

