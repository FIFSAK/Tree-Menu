from django.shortcuts import render
from .models import MenuItem


def main_view(request):
    menus = MenuItem.objects.filter(parent__isnull=True)
    current_path = request.path
    context = {'current_path': current_path, 'page_title': 'О нас'}
    return render(request, 'base.html', context)


def about_view(request):
    current_path = request.path
    context = {'current_path': current_path, 'page_title': 'О нас'}
    return render(request, 'base.html', context)

# Повторите это для каждого view, где передаётся context



def contacts_view(request):
    current_path = request.path
    context = {'current_path': current_path, 'page_title': 'Контакты'}
    return render(request, 'base.html', context)


def menu_view(request):
    current_path = request.path
    context = {'current_path': current_path, 'page_title': 'Меню'}
    return render(request, 'base.html', context)