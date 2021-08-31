from django.urls import path
from .views import BlogView, PostDetailView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', EditPostView.as_view(), name='edit_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post')]
