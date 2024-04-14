from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url_name = models.CharField(max_length=100, blank=True, null=True)  # Имя именованного URL
    url = models.CharField(max_length=200, blank=True, null=True)  # Явный URL

    def get_absolute_url(self):
        if self.url_name:
            try:
                return reverse(self.url_name)
            except NoReverseMatch:
                return "#"
        return self.url if self.url else "#"

    def __str__(self):
        return self.name
