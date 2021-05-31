from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogView(ListView):
    model = Post
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

