from django.shortcuts import render, get_list_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    posts = get_list_or_404(Post, slug=post, status='published',
                            publish_year=year, publish_month=month, publish_day=day)

    return render(request, 'blog/post/list.html', {'posts': posts})
