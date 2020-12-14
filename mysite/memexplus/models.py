from django.db import models


class Bookmark(models.Model):
    url = models.CharField(max_length=2000)


class BasicBookmark(Bookmark):
    full_text = models.TextField()
    stripped_text = models.TextField()
