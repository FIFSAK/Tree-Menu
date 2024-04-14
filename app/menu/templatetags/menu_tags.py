from django import template
from django.template.loader import render_to_string
from ..models import MenuItem
from django.utils.safestring import mark_safe
from django.db.models import Prefetch

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    top_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related(
        Prefetch('children', queryset=MenuItem.objects.all().prefetch_related('children'))
    )
    menu_items = process_menu_hierarchy(top_items, current_url)
    rendered_menu = render_to_string('menu_template.html', {'menu_items': menu_items})
    return mark_safe(rendered_menu)


def process_menu_hierarchy(items, current_url, ancestors_open=False):
    menu_list = []
    for item in items:
        item_url = item.get_absolute_url() or "/"
        is_active = current_url.startswith(item_url) if item_url != '/' else current_url == item_url
        children = item.children.all()
        children_menu = process_menu_hierarchy(children, current_url, ancestors_open=is_active or ancestors_open)
        expand = is_active or ancestors_open

        menu_obj = {
            'name': item.name,
            'url': item_url,
            'children': children_menu,
            'is_active': is_active,
            'expand': expand,
        }
        menu_list.append(menu_obj)
    return menu_list




