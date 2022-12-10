from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group

QUANTITY_OF_POSTS = 10


def index(request):

    # получение списка постов в обратном порядке.
    post_list = Post.objects.all().order_by('-pub_date')
    # по 10 постов на странице.
    paginator = Paginator(post_list, 10)
    # извлечение № страницы из URL - значение параметра page.
    page_number = request.GET.get('page')
    # получение набора записей с нужной страницы.
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
    paginator = Paginator(group_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj,
    }

    return render(request, template, context)
