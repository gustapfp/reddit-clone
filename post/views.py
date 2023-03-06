from django.shortcuts import render
from rest_framework import viewsets
from post.models import Post
from post.serializer import PostSerializer
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