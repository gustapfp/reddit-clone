from django.shortcuts import render
from rest_framework import viewsets
from post.models import Post, Comment
from post.serializer import PostSerializer, CommentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return render(request, 'post/index.html')

class PostViewSet(viewsets.ModelViewSet):
    """ 
    List all posts created

    Args:
        viewsets (_type_): _description_
    """
    queryset = Post.objects.all()
    serializer_class =  PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """ 
    List all coments created

    Args:
        viewsets (_type_): _description_
    """
    queryset = Comment.objects.all()
    serializer_class =  CommentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]