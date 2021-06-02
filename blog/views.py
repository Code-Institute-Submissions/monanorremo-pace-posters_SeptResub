from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-created_on']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_post.html'
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')
