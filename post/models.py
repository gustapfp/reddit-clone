from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    topic = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title