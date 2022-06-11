from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', null = True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() #Def manager
    published = PublishedManager() #Published manager

    class Meta:
        ordering = ('-publish', )

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    
    def __str__(self):
        return self.title


