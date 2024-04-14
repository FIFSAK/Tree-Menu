from django.contrib import admin
from django.urls import path
from menu.views import home_view, menu_detail_view


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('menu/<str:url_name>/', menu_detail_view, name='menu_detail'),
]

