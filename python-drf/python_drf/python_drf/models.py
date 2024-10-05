from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=256)


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    url = models.TextField()
    categories = models.ManyToManyField(Category)
