from django.shortcuts import render, get_object_or_404
from .models import MenuItem


def home_view(request):
    root_menus = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'home.html', {'menus': root_menus})


def menu_detail_view(request, url_name):
    root_menu = get_object_or_404(MenuItem, url_name=url_name, parent__isnull=True)
    menu_items = root_menu.children.all()
    return render(request, 'menu_detail.html', {'menu_items': menu_items, 'menu': root_menu})
