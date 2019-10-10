from rest_framework import serializers
from .models import Posts,Category




class PostSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source='category.title')
    category_description = serializers.ReadOnlyField(source='category.description')
    class Meta:
        model = Posts
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields =['status','posts']
        