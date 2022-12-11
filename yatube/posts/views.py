from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User

Q_OF_POSTS = 10


def index(request):

    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, Q_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = 'Последние обновления!'
    template = 'posts/index.html'

    context = {
        'page_obj': page_obj,
        'title': title,
    }

    return render(request, template, context)


def group_posts(request, slug):

    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    group_list = group.posts.all().order_by('-pub_date')
    paginator = Paginator(group_list, Q_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj,
    }

    return render(request, template, context)


def profile(request, username):

    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    post_count = Post.objects.filter(author=author).count()
    paginator = Paginator(posts, Q_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = (f'Профайл пользователя {author}')
    template = 'posts/profile.html'

    context = {
        'page_obj': page_obj,
        'title': title,
        'author': author,
        'posts': posts,
        'post_count': post_count,
    }
    return render(request, template, context)


def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    template = 'posts/post_detail.html'
    title = post.text[30]

    context = {
        'post': post,
        'title': title
    }
    return render(request, template, context)
