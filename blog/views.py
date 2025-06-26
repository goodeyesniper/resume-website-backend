from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all().order_by('-date')
    serializer_class = BlogPostSerializer