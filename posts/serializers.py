from rest_framework import serializers
from .models import Posts,Category

# class FilteredPostSerializer(serializers.ListSerializer):
#     def to_representation(self,data):
#        data = data.filter(status=True)
#        return super(FilteredPostSerializer,  self).to_representation(data)


class PostSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source='category.title')
    category_description = serializers.ReadOnlyField(source='category.description')
    class Meta:
        model = Posts
        #list_serializer_class = FilteredPostSerializer
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields ="__all__"
        