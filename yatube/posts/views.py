from django.shortcuts import render, get_object_or_404
from .models import Post, Group

QUANTITY_OF_POSTS = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:QUANTITY_OF_POSTS]
    title = 'Это главная страница проекта Yatube'
    template = 'posts/index.html'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:QUANTITY_OF_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
