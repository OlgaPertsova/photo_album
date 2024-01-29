from django.db import models


class Photos(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=400)
    image = models.ImageField(upload_to='photos/images/')
    url = models.URLField(blank=True)
