from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Posts,Category
from .serializers import PostSerializer,CategorySerializer
# Create your views here.
@api_view()
def posts(request):
    if request.method=="GET":
        posts=Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view()
def category(request):
    if request.method=="GET":
        category=Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)        

def post_html(request):
    return render(request,'index.html')