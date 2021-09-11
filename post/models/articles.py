from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)
    aproved_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    