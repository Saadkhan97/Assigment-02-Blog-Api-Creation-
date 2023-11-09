from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

from rest_framework import serializers
from .models import *

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('title', 'content')
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text','blog_post')