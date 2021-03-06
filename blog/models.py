from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)