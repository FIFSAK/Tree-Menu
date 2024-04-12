from django.shortcuts import render
from .models import Folder
from django.http import HttpResponse
from django.core import serializers


def get_menu(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            # Получаем все корневые папки, если pk не указан
            folders = Folder.objects.filter(parent=None)
        else:
            # Или одну конкретную папку по pk
            folders = [Folder.objects.get(id=pk)]

        # Подготавливаем контекст для шаблона
        context = {'folders': []}
        for folder in folders:
            subfolders = Folder.objects.get_all_subfolders(folder)
            context['folders'].append({'folder': folder, 'subfolders': subfolders})
        return render(request, 'menu.html', context)
