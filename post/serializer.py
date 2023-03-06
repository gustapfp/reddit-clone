from rest_framework import serializers
from post.models import Post, Comment

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comment
        fields = '__all__'

class ListingCommentPostSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source="post.title")

    class Meta:
        model = Comment
        fields = ['post']

