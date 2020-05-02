from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', related_name='comments_made', on_delete=models.CASCADE)
    body = models.TextField()
    

class Author(models.Model):
    user = models.OneToOneField(User, related_name='author', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name