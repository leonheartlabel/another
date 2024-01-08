
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField( default='')
    stars = models.FloatField(default=0)
    price = models.FloatField(default=0)
    title = models.TextField(max_length=255)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title