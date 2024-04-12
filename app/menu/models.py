from django.db import models


class FolderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_all_subfolders(self, folder):
        subfolders = folder.children.all()
        for subfolder in subfolders:
            subfolders = subfolders.union(self.get_all_subfolders(subfolder))
        return subfolders


class Folder(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    objects = FolderManager()

    def __str__(self):
        return self.name
