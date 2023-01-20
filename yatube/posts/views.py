"""Функции отображения страниц."""

from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    """Функция главной страницы."""
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница'
    text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
        'text': text
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Функция страницы группы."""
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    title = f'Группа {slug}'
    text = f'Страница группы {slug}'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'text': text
    }
    return render(request, template, context)
