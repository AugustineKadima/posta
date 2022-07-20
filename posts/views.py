from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer



   