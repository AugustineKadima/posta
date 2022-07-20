from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users":reverse("user-list", request=request, format=format),
        "posts":reverse("post-list", request=request, format=format)
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]




   