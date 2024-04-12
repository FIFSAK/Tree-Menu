from django.shortcuts import render
from django.http import HttpResponse
from .models import Folder, FolderManager
from django.core import serializers


def get_menu(request, pk=None):
    if request.method == 'GET':
        folder = Folder.objects.get(parent=pk)
        subfolders = Folder.objects.get_all_subfolders(folder)
        return render(request, 'menu.html', {'subfolders': subfolders, 'folder': folder})
        # return HttpResponse(serializers.serialize('json', subfolders))
