from django.shortcuts import render
from .models import MenuItem


def home_view(request):
    # Получаем все корневые элементы меню
    root_menus = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'home.html', {'menus': root_menus})


# views.py

from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def menu_detail_view(request, url_name):
    # Получаем корневой пункт меню по ID
    root_menu = get_object_or_404(MenuItem, url_name=url_name, parent__isnull=True)
    # Получаем все дочерние пункты меню для данного корневого элемента
    menu_items = root_menu.children.all()
    return render(request, 'menu_detail.html', {'menu_items': menu_items, 'menu': root_menu})



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
