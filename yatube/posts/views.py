from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Post, Group

QUANTITY_OF_POSTS = 10


@login_required
def index(request):
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к
    # меньшим)
    posts = Post.objects.order_by('-pub_date')[:QUANTITY_OF_POSTS]
    title = 'Это главная страница проекта Yatube'
    template = 'posts/index.html'

    context = {
        'posts': posts,
        'title': title,

    }
    return render(request, template, context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = (
        Post.objects.filter(group=group)
        .order_by('-pub_date')[:QUANTITY_OF_POSTS]
    )
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
