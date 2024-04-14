from django.contrib import admin
from django.urls import path
from menu.views import about_view, contacts_view, menu_view, home_view, menu_detail_view


urlpatterns = [
    path('', home_view, name='home'),
    path('menu/<str:url_name>/', menu_detail_view, name='menu_detail'),
]

