from django.db import models
from django.contrib.auth.models import User


# STATUS = (
#     (0,"Draft"),
#     (1,"Publish"),
#     (3,"Review")
# )

class Lesson(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='article_post')
    updated_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='article_update', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    status = models.ForeignKey('Lessonstatus', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class LessonStatus(models.Model):
    label = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.label