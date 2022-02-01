from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Posts
from .serializer import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
