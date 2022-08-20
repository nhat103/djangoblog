from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class PuslishedManager(models.Model):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().fille(status='pushlished')


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.TextField(
        max_length=10, choices=STATUS_CHOICE, default='draft')
    objects = models.Manager()
    publish = PuslishedManager()


class Meta:
    oderring = ('-publish')


def __str__(self):
    return self.title
