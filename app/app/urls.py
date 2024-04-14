from django.contrib import admin
from django.urls import path
from menu.views import main_view, about_view, contacts_view, menu_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='menus'),
    path('about/', about_view, name='about'),
    path('contacts/', contacts_view, name='contacts'),
    path('menu/', menu_view, name='menu'),

]
