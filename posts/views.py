from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Posts,Category
from .serializers import PostSerializer,CategorySerializer
from django.http import JsonResponse,HttpResponse
# Create your views here.
@api_view()
def posts(request):
    if request.method=="GET":
        posts=Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def category(request):
    if request.method=="POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':201})
        return Response({'errors':serializer.errors,'status':400})
    else:
        category=Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)       

def post_html(request):
    return render(request,'index.html')