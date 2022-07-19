from django.db import models

# Create your models here.


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=30, blank=False)

    class Meta:
        ordering = ["created"]