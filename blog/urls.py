from django.urls import path
from .views import BlogPostListAPIView

urlpatterns = [
    path('posts/', BlogPostListAPIView.as_view(), name='blogpost-list'),
]