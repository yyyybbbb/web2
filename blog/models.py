from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICE = (("draft", "DRAFT"), ("published", "PUBLISHED"),)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    author = models.ForeignKey(User, related_name="blog_posts")
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="draft")

    class Meta:
        ordering = ("-published",)    #注意这里的元组，其中如果是一个元素，后面必须有逗号。

    def __str__(self):
        return self.title
